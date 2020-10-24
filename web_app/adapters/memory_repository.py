from bisect import insort_left

from web_app.adapters.repository import AbstractRepository
from web_app.domainmodel.movie import Movie
from web_app.domainmodel.user import User
from web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__movies = list()
        self.__movie_index = dict()
        self.__users = list()

    def get_movie(self, id: int):
        if id not in self.__movie_index.keys():
            return None
        else:
            return self.__movie_index[id]

    def add_movie(self, movie: Movie):
        insort_left(self.__movies, movie)
        self.__movie_index[movie.id] = movie

    def get_movies_for_browse(self, id_list):
        real_ids = [id for id in id_list if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]

    def get_ids_of_movies(self):
        return [i for i in self.__movie_index.keys()]

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self.__users if user.user_name == username), None)


def populate(filename, repo):
    csv = MovieFileCSVReader(filename)
    csv.read_csv_file()
    for movie in csv.dataset_of_movies:
        repo.add_movie(movie)