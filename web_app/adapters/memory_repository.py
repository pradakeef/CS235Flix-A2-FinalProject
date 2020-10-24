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
        self.__genres = list()
        self.__actors = list()
        self.__directors = list()
        self.__release_years = list()
        self.__genre_pop = dict()
        self.__reviews = list()

    def get_movie(self, id: int):
        if id not in self.__movie_index.keys():
            return None
        else:
            return self.__movie_index[id]

    def get_genres(self) -> list:
        return self.__genres

    def get_actors(self) -> list:
        return self.__actors

    def get_directors(self) -> list:
        return self.__directors

    def get_release_years(self) -> list:
        return self.__release_years

    def get_size_of_genre(self, a_genre: 'Genre') -> int:
        return self.__genre_pop[a_genre]

    def add_genre(self, a_genre: 'Genre'):
        self.__genres.append(a_genre)
        if a_genre not in self.__genre_pop:
            self.__genre_pop[a_genre] = 0

    def add_actor(self, a_actor: 'Actor'):
        self.__actors.append(a_actor)

    def add_director(self, a_director: 'Director'):
        self.__directors.append(a_director)

    def add_release_year(self, a_year: int):
        self.__release_years.append(a_year)

    def tidy_up(self) -> None:
        self.__movies.sort()
        self.__directors.sort()
        self.__actors.sort()
        self.__genres.sort()
        self.__release_years.sort()

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