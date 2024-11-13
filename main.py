from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv



storage = StorageJson("preethi_movicatalog.json")
movie_app = MovieApp(storage)
movie_app.run()
storage_csv = StorageCsv("movies.csv")
movie_app1 = MovieApp(storage_csv)
movie_app1.run()


