from scripts.serializedata import SerializeData
from storage.istorage import IStorage
import os
import json
import random

class StorageJson(IStorage):
    def __init__(self,file_path):
        self.file_path = file_path

    def update_json(self,movie_list):
        """Update the JSON file with the modified movie list."""
        with open(self.file_path, "w", encoding="utf-8") as handle:
            json.dump(movie_list, handle, indent=4)

    def search_movie(self,search_item):
        """Search for movies containing the search term in the title."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if search_item.lower() in movie["title"].lower():
                print(f"{movie['title']}, {movie['rating']}")

    def list_movies(self):
        # Check if the file exists; if not, create it with an empty list
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as handle:
                json.dump([], handle)

        # Try to open and read the JSON file
        with open(self.file_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        return data

    def movie_sorted_by_rating(self):
        """Display movies sorted by rating in descending order."""
        movie_list = self.list_movies()
        rate_sorted = sorted(movie_list, key=lambda x: float(x["rating"]), reverse=True)
        for movies in rate_sorted:
            print(f"Movie Title: {movies['title']}  Movie Year: {movies['year']}  "
                  f"Movie Rating: {movies['rating']}")
            print("-" * 100)

    def filter_movies(self, user_rating, start_year, end_year):
        """Filter and display movies with a given rating."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["rating"] >= user_rating and start_year <= movie["year"] <= end_year:
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

    def add_movie(self,movie_name, movie_year, movie_rating, poster,imdb_movielink, movie_notes):
        """Add a new movie to the list and update the JSON file."""
        movie_dict = {
            "title": movie_name,
            "year": movie_year,
            "rating": movie_rating,
            "poster":poster,
            "imdbmovielink":imdb_movielink,
            "movienotes": movie_notes
        }
        data = self.list_movies()
        data.append(movie_dict)
        self.update_json(data)

    def stats(self):
        """Calculate and display movie statistics like average and median ratings."""
        movie_list = self.list_movies()
        return movie_list

    def delete_movie(self,movie_name):
        """Delete a movie from the list and update the JSON file."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if movie["title"] == movie_name:
                movie_list.remove(movie)
        self.update_json(movie_list)

    def random_movies(self):
        """Pick and display a random movie."""
        movie_list = self.list_movies()
        random_movie = random.choice(movie_list)

        # Display the randomly selected movie details
        print("Randomly Selected Movie:")
        print(f"Title: {random_movie['title']}")
        print(f"Rating: {random_movie['rating']}")
        print(f"Year: {random_movie['year']}")

    def update_movie(self,movie_name, movie_note):
        """Update the rating of a movie and update the JSON file."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["title"] == movie_name:
                movie["movienotes"] = movie_note
        self.update_json(movie_list)


    def generate_website(self):
        result = ""
        movie_data = self.list_movies()
        for index,movie in enumerate(movie_data):
            result += SerializeData.serialize_movie(movie)
        SerializeData.write_newhtml(result)
