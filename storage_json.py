from istorage import IStorage
import os
import json

class StorageJson(IStorage):
    def __init__(self,file_path):
        self.file_path = file_path

    def update_json(self,movie_list):
        """Update the JSON file with the modified movie list."""
        with open(self.file_path, "w") as handle:
            json.dump(movie_list, handle, indent=4)

    def list_movies(self):
        # Check if the file exists; if not, create it with an empty list
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as handle:
                json.dump([], handle)

        # Try to open and read the JSON file
        with open(self.file_path, "r") as handle:
            data = json.load(handle)
        return data

    def add_movie(self,movie_name, movie_year, movie_rating, poster):
        """Add a new movie to the list and update the JSON file."""
        movie_dict = {
            "title": movie_name,
            "year": movie_year,
            "rating": movie_rating
        }
        data = self.list_movies()
        data.append(movie_dict)
        self.update_json(data)

    def delete_movie(self,movie_name):
        """Delete a movie from the list and update the JSON file."""
        movie_list = self.list_movies()

        for movie in movie_list:
            if movie["title"] == movie_name:
                movie_list.remove(movie)
        self.update_json(movie_list)

    def update_movie(self,movie_name, new_rating):
        """Update the rating of a movie and update the JSON file."""
        movie_list = self.list_movies()
        for movie in movie_list:
            if movie["title"] == movie_name:
                movie["rating"] = new_rating
        self.update_json(movie_list)