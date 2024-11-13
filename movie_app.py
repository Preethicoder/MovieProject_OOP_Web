display_menu = """********** My Movies Database **********

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

Enter choice (1-10): """

class MovieApp:
    def __init__(self,storage):
        self._storage = storage

    def is_present(self,movie_name):
        """Check if a movie is present in the database."""
        movie_list = self._storage.list_movies()
        return any(movie["title"] == movie_name for movie in movie_list)

    def _command_add_movie(self):
        """Add a new movie to the database."""
        movie_name = input("Enter movie name: ")
        if movie_name.isspace():
            print("Empty string not allowed")
            return
        movie_year = input("Enter movie year: ")
        movie_rating = input("Enter movie rating: ")

        if self.is_present(movie_name):
            print(f"The movie '{movie_name}' is already present.")
        else:
            self._storage.add_movie(movie_name,movie_year,movie_rating,"")
            print("Movie added successfully.")

    def _command_delete_movie(self):
        """Delete a movie from the database."""
        delete_moviename = input("Enter the movie name to be deleted: ")
        if self.is_present(delete_moviename):
            self._storage.delete_movie(delete_moviename)
            print("Movie deleted successfully.")
        else:
            print("Movie name not present.")

    def _command_update_movie(self):
        """Update the rating of an existing movie."""
        movie_name = input("Enter the movie name to be updated: ")
        if self.is_present(movie_name):
            new_rating = input("Enter new rating: ")
            self._storage.update_movie(movie_name, new_rating)
            print("Movie rating updated.")
        else:
            print("Movie name not present.")

    def _command_list_movies(self):
        """get list of movies from IStorage"""
        movies = self._storage.list_movies()
        print (movies)


    def run(self):
        func_dict = {
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie
        }
        """Main function to display the menu and handle user inputs."""
        print(display_menu)
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
            print(display_menu)