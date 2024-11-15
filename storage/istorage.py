from abc import ABC , abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        pass

    @abstractmethod
    def delete_movie(self,title):
        pass

    @abstractmethod
    def update_movie(self,title,rating):
        pass

    @abstractmethod
    def stats(self):
        pass

    @abstractmethod
    def random_movies(self):
        pass

    @abstractmethod
    def search_movie(self,movie_name):
        pass
    @abstractmethod
    def movie_sorted_by_rating(self):
        pass

    @abstractmethod
    def movie_sorted_by_year(self):
        pass

    @abstractmethod
    def filter_movies(self, user_rating, start_year, end_year):
        pass

    @abstractmethod
    def generate_website(self):
        pass

