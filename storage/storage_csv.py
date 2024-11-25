from scripts.serializedata import SerializeData
from storage.istorage import IStorage
import os
import csv
import random

class StorageCsv(IStorage):
    def __init__(self,file_name):
        self.file_name = file_name
        print("csv",file_name)

    def add_movie(self, title, year, rating, poster,imdbmovielink,movienotes):
        """Add a new movie to the list and update the JSON file."""
        movie_dict = {
            "title": title,
            "year": year,
            "rating": rating,
            "poster": poster,
            "imdbmovielink": imdbmovielink,
            "movienotes": movienotes
        }
        data = self.list_movies()
        data.append(movie_dict)
        self.update_csv(data)

    def delete_movie(self,title):
        """Delete a movie from the list and update the JSON file."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if movie["title"] == title:
                movie_list.remove(movie)
        self.update_csv(movie_list)

    def update_movie(self,title,movie_note):
        """Update the rating of a movie and update the JSON file."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["title"] == title:
                movie["movienotes"] = movie_note
        self.update_csv(movie_list)

    def stats(self):
        """Calculate and display movie statistics like average and median ratings."""
        movie_list = self.list_movies()
        return  movie_list


    def list_movies(self):
        """
           Reads and returns a list of movies from the CSV file.
           If the file doesn't exist, it creates one with the appropriate headers.
           """
        data = []

        # Check if the file exists; if not, create it with headers
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode="w", newline="", encoding="utf-8") as fileobj:
                writer = csv.DictWriter(fileobj,
                                        fieldnames=["title", "year", "rating", "poster", "imdbmovielink", "movienotes"])
                writer.writeheader()
            return data  # Return an empty list for a new file

        # Open the file and read data
        with open(self.file_name, "r", encoding="utf-8") as filehandle:
            reader = csv.DictReader(filehandle)
            for row in reader:
                 data.append(row)

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
        """Overwrite the CSV file with the updated data."""
        with open(self.file_name, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["title", "year", "rating", "poster", "imdbmovielink", "movienotes"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movie_list)


    def generate_website(self):
        """Used to generate a html after serializing data"""
        result = ""
        movie_data = self.list_movies()
        for index, movie in enumerate(movie_data):
            result += SerializeData.serialize_movie(movie)
        SerializeData.write_newhtml(result)

