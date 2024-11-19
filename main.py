from storage.storage_csv import StorageCsv
from storage.storage_json import StorageJson
from movie_app import MovieApp
import sys




if __name__ == "__main__":
    n = len(sys.argv)
    if n < 2:
        print("Usage: python3 main.py <file.json/csv>")
        sys.exit(1)

    for x in range(1, n):
        try:
            file_name = sys.argv[x]
            if file_name.endswith(".json"):
                storage = StorageJson(f"data/{file_name}")
            elif file_name.endswith(".csv"):
                storage = StorageCsv(f"data/{file_name}")
            else:
                print(f"Invalid argument: {file_name}. Please provide a .json or .csv file.")
                continue

            movie_app = MovieApp(storage)
            movie_app.run()
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

"""storage = StorageJson("data/preethi_movicatalog.json")
movie_app = MovieApp(storage)
movie_app.run()"""
"""storage_csv = StorageCsv("data/movies.csv")
movie_app1 = MovieApp(storage_csv)
movie_app1.run()"""




