import abc


from web_app.domainmodel.movie import Movie
from web_app.domainmodel.user import User


repository_instance = None


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_movie(self, id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_for_browse(self, id_list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_ids_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError