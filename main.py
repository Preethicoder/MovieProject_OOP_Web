from storage.storage_csv import StorageCsv
from storage.storage_json import StorageJson
from movie_app import MovieApp
import sys

n = len(sys.argv)
for x in range(1,n):
    if ".json" in sys.argv[x]:
        file_name = sys.argv[x]
        storage = StorageJson(f"data/{file_name}")
        movie_app = MovieApp(storage)
        movie_app.run()
    elif ".csv" in sys.argv[x]:
        file_name = sys.argv[x]
        storage = StorageCsv(f"data/{file_name}")
        movie_app = MovieApp(storage)
        movie_app.run()


"""storage = StorageJson("data/preethi_movicatalog.json")
movie_app = MovieApp(storage)
movie_app.run()"""
"""storage_csv = StorageCsv("data/movies.csv")
movie_app1 = MovieApp(storage_csv)
movie_app1.run()"""




