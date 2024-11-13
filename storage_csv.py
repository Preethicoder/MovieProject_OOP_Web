from istorage import IStorage
import os
import csv

class StorageCsv(IStorage):
    def __init__(self,file_name):
        self.file_name = file_name

    def add_movie(self, title, year, rating, poster):
        pass

    def delete_movie(self,title):
        pass

    def update_movie(self,title,rating):
        pass

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


    def update_csv(self):
        pass

