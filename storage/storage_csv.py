from storage.istorage import IStorage
import os
import csv
import random

class StorageCsv(IStorage):
    def __init__(self,file_name):
        self.file_name = file_name

    def add_movie(self, title, year, rating, poster):
        """Add a new movie to the list and update the JSON file."""
        movie_dict = {
            "title": title,
            "year": year,
            "rating": rating,
            "poster":poster
        }
        data = self.list_movies()
        print("data:::",data)
        data.append(movie_dict)
        self.update_csv(data)

    def delete_movie(self,title):
        """Delete a movie from the list and update the JSON file."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if movie["title"] == title:
                movie_list.remove(movie)
        self.update_csv(movie_list)

    def update_movie(self,title,rating):
        """Update the rating of a movie and update the JSON file."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["title"] == title:
                movie["rating"] = rating
        self.update_csv(movie_list)

    def stats(self):
        """Calculate and display movie statistics like average and median ratings."""
        movie_list = self.list_movies()
        ratings =[float(movie["rating"])if movie["rating"] != "N/A" else 0.0 for movie in movie_list]
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

    def list_movies(self):
        data = []
        if not os.path.exists(self.file_name):
            with open(self.file_name,mode="w",newline="")as fileobj:
                csv.DictWriter(fileobj,"")

        with open(self.file_name,"r") as filehandle:
            reader = csv.DictReader(filehandle)
            for info in reader:
                data.append(dict(info))

        return data

    def movie_sorted_by_rating(self):
        """Display movies sorted by rating in descending order."""
        movie_list = self.list_movies()
        rate_sorted = sorted(movie_list, key=lambda x: float(x["rating"]), reverse=True)
        for movies in rate_sorted:
            print(f"Movie Title: {movies['title']}  Movie Year: {movies['year']}  "
                  f"Movie Rating: {movies['rating']}")
            print("-" * 100)

    def filter_movies(self,user_rating, start_year, end_year):
        """Filter and display movies with a given rating."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["rating"] >= user_rating and movie["year"] >= start_year and movie["year"] <= end_year:
                print(f"Movie Title: {movie['title']}  Movie Year: {movie['year']}  "
                      f"Movie Rating: {movie['rating']}")
                print("-" * 100)


    def movie_sorted_by_year(self):
        """Display movies sorted by release year in descending order."""
        movie_list = self.list_movies()
        year_sorted = sorted(movie_list, key=lambda x: x["year"], reverse=True)
        for movies in year_sorted:
            print(f"Movie Title: {movies['title']}  Movie Year: {movies['year']}  "
                  f"Movie Rating: {movies['rating']}")
            print("-" * 100)
    def search_movie(self,search_item):
        """Search for movies containing the search term in the title."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if search_item.lower() in movie["title"].lower():
                print(f"{movie['title']}, {movie['rating']}")

    def random_movies(self):
        """Pick and display a random movie."""
        movie_list = self.list_movies()
        random_movie = random.choice(movie_list)

        # Display the randomly selected movie details
        print("Randomly Selected Movie:")
        print(f"Title: {random_movie['title']}")
        print(f"Rating: {random_movie['rating']}")
        print(f"Year: {random_movie['year']}")

    def update_csv(self,movie_list):
        """Overwrite the CSV file with a new list of movies."""
        with open(self.file_name, mode="w", newline="") as fileobj:
            writer = csv.DictWriter(fileobj, fieldnames=["title", "year", "rating","poster"])
            writer.writeheader()
            writer.writerows(movie_list)

    def serialize_movie(self, movie):
        """Serialize and create html tag for each item"""
        output = ''
        output += f'<li>\n'
        output += f'<div class="movie">\n'
        output += f'<img class="movie-poster" src={movie["poster"]}/>\n'
        output += f'<div class="movie-title">{movie["title"]}</div>\n'
        output += f'<div class="movie-year">{movie["year"]}</div>\n'
        output += '</div>\n'
        output += '</li>'
        return output

    def write_newhtml(self, result):
        """with new generate data it create new html file"""
        with open("../_static/index_template.html", "r") as handle:
            html_content = handle.read()

        html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", result)
        html_content = html_content.replace("__TEMPLATE_TITLE__", "My Favorite movies")

        with open("../_static/movie_website.html", "w") as handle1:
            handle1.write(html_content)

    def generate_website(self):
        result = ""
        movie_data = self.list_movies()
        for index, movie in enumerate(movie_data):
            result += self.serialize_movie(movie)
        self.write_newhtml(result)

