from storage_json import StorageJson
from movie_app import MovieApp


storage = StorageJson("movie_catalog.json")
movie_app = MovieApp(storage)
movie_app.run()


