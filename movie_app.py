import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISPLAY_MENU = """********** My Movies Database **********

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Filter movies by rating
11. Generate Website

Enter choice (1-11): """
API_KEY = os.getenv('API_KEY')


class MovieApp:
    def __init__(self, storage):
        """to initilaize the object to corresponding class"""
        self._storage = storage

    def is_present(self, movie_name):
        """Check if a movie is present in the database."""
        movie_list = self._storage.list_movies()
        return any(movie["title"] == movie_name for movie in movie_list)

    @staticmethod
    def fetch_data( movie_name):
        """fetch data about the user given movie_name"""
        url = "http://www.omdbapi.com/"
        params = {
            'apikey': API_KEY,
            't': movie_name
        }
        try:
            res = requests.get(url, params=params,  timeout=10)
            data = res.json()
            if data.get('Response') == 'False':
                print("Movie not found")
                return None
            return data
        except requests.exceptions.ConnectionError as ne:
            print("Network error occurred 1::", ne)
            return None
        except requests.exceptions.RequestException as e:
            print("Network error occurred::", e)
            return None

    @staticmethod
    def fetch_movielink(imdb_movieid):
        """based on the imdb_id it creates the url link for the movie"""
        imdb_id = imdb_movieid
        imdb_url = f"https://www.imdb.com/title/{imdb_id}/"

        return imdb_url

    def _command_add_movie(self):
        """Add a new movie to the database."""
        movie_name = input("Enter movie name: ")
        if movie_name.isspace():
            print("Empty string not allowed")
            return
        data = self.fetch_data(movie_name)
        if data is None:
            return
        if data["imdbID"] != " ":
            movie_link = self.fetch_movielink(data["imdbID"])
        else:
            movie_link = ""
        movie_name = data["Title"]
        movie_year = data["Year"]
        movie_rating = data["imdbRating"]
        movie_poster = data["Poster"]
        imdb_link = movie_link

        if self.is_present(movie_name):
            print(f"The movie '{movie_name}' is already present.")
        else:
            self._storage.add_movie(movie_name, movie_year,
                                    movie_rating, movie_poster, imdb_link, "")
            print("Movie added successfully.")

    def _command_delete_movie(self):
        """Delete a movie from the database."""
        delete_movie_name = input("Enter the movie name to be deleted: ")
        if self.is_present(delete_movie_name):
            self._storage.delete_movie(delete_movie_name)
            print("Movie deleted successfully.")
        else:
            print("Movie name not present.")

    def _command_update_movie(self):
        """Update the rating of an existing movie."""
        movie_name = input("Enter the movie name to be updated: ")
        if self.is_present(movie_name):
            movie_note = input("Enter movie note: ")
            self._storage.update_movie(movie_name, movie_note)
            print("Added Movie note.")
        else:
            print("Movie name not present.")

    def _command_list_movies(self):
        """get list of movies from IStorage"""
        movies = self._storage.list_movies()
        for index,movie in enumerate(movies):
            print(f"{index + 1}:{movie['title']}  Rating:{movie['rating']}")

    def _command_stats(self):
        movie_list =self._storage.stats()
        ratings = [float(movie["rating"])
                   if movie["rating"] != "N/A" else 0.0 for movie in movie_list]
        avg_rating = sum(ratings) / len(ratings)
        print(f"Average rating: {avg_rating:.2f}")

        sorted_rating = sorted(ratings)
        n = len(sorted_rating)
        if n % 2 == 1:
            median_rating = sorted_rating[n // 2]
        else:
            mid1 = sorted_rating[n // 2 - 1]
            mid2 = sorted_rating[n // 2]
            median_rating = (mid1 + mid2) / 2
        print(f"Median Rating: {median_rating:.2f}")

        # Maximum and minimum rated movies
        maximum_rating = max(ratings)
        for movie in movie_list:
            if float(movie["rating"]) == maximum_rating:
                print(f"Maximum rated Movie: {movie['title']}")

        minimum_rating = min(ratings)
        for movie in movie_list:
            if float(movie["rating"]) == minimum_rating:
                print(f"Minimum rated Movie: {movie['title']}")

    def _command_random_movies(self):
        self._storage.random_movies()

    def _command_search_movie(self):
        movie_name = input("Enter the movie name to be searched: ")
        self._storage.search_movie(movie_name)

    def _command_movies_sorted_by_rating(self):
        self._storage.movie_sorted_by_rating()

    def _command_movie_sorted_by_year(self):
        self._storage.movie_sorted_by_year()

    def _command_filter_movies(self):
        """Filter movies based on user rating."""
        user_rating = input("Enter minimum rating:")
        start_year = input("Enter start year:")
        end_year = input("Enter end year:")
        self._storage.filter_movies(user_rating, start_year, end_year)

    def _command_generate_website(self):
        self._storage.generate_website()
        print("Website was successfully generated to the file movie_website.html")

    def run(self):
        """Main function to display the menu and handle user inputs."""
        func_dict = {
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_stats,
            "6": self._command_random_movies,
            "7": self._command_search_movie,
            "8": self._command_movies_sorted_by_rating,
            "9": self._command_movie_sorted_by_year,
            "10": self._command_filter_movies,
            "11": self._command_generate_website

        }

        print(DISPLAY_MENU)
        while True:
            try:
                user_input = input("Enter your choice: ").strip()

                if user_input == "0":
                    print("Bye!")
                    break

                # Retrieve the function associated with the user input
                func_id = func_dict.get(user_input)

                if func_id:
                    # Call the selected function
                    func_id()
                else:
                    # If user_input is not in func_dict or 0, print an error message
                    print("Invalid option. Please enter a valid choice.")

            except KeyError:
                print("Invalid option. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")

            except Exception as e:
                # Catch any other unexpected errors and display them
                print(f"An unexpected error occurred: {e}")

            # Display the menu again for the next round of input
            input("\nPress Enter to display the menu...")
            print(DISPLAY_MENU)
