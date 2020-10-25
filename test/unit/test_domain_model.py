import pytest

from web_app.domainmodel.actor import Actor
from web_app.domainmodel.genre import Genre
from web_app.domainmodel.movie import Movie
from web_app.domainmodel.review import Review
from web_app.domainmodel.watchlist import WatchList
from web_app.domainmodel.user import User



def test_director_genre_actor():
    # check_init
    director = Director("Christopher Nolan")
    actor = Actor("Chris Pratt")
    genre = Genre("Horror")
    print(director)
    print(actor)
    print(genre)


def test_movie():
    # check_boolean_equality_function
    movie = Movie("Moana", 2009)
    print(movie)

    movie3 = Movie("Moana", 2010)
    print(movie3)

    movie2 = Movie("Inception", 2010)
    print(movie2)

    print(movie > movie2)
    print(movie < movie3)
    print(movie3 == movie3)

    # check_remove_actor_in_list_of_actors
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    movie.remove_actor(Actor("Auli'i Cravalho"))
    print(movie.actors)

    # check_for_out_of_range_runtime
    movie.runtime_minutes = 121
    print("Movie runtime: {} minutes".format(movie.runtime_minutes))

    movie.external_rating = 30
    print("votes: {}".format(movie.external_rating))



def test_review():
    # check_not_review_type_and_rating_returns_none
    movie = Movie("Moana", 2016)
    review_text = Movie("Me", 2324)
    rating = 100
    review = Review(movie, review_text, rating)

    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))

    # check_same_review_equality
    movie = Movie("Moana", 2016)
    review_text = "It was a very fun movie for the kids"
    rating = 8.1
    review = Review(movie, review_text, rating)
    review2 = Review(movie, review_text, rating)

    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))

    print(review2 == review)
    print(review == review2)
    print(review2.timestamp)
    print(review.timestamp)


def test_user():
    user1 = User('Martin', 'pw12345')
    user4 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Daniel', 'pw87465')

    movie = Movie("Moana", 2009)
    review_text = "It was so average"
    rating = 10
    review = Review(movie, review_text, rating)
    print(movie)
    movie.runtime_minutes = 107

    movie3 = Movie("", 4545)
    print(movie3)

    movie2 = Movie("Inception", 2010)
    movie2.runtime_minutes = 133
    user1.watch_movie(movie)
    user1.watch_movie(movie2)
    user1.watch_movie(movie)
    user2.add_review(review)
    print(user1)
    print(user4)
    print(user2)
    print(user3)
    print(user1 == user4)
    print(user1 > user2)
    print(user1.time_spent_watching_movies_minutes)
    print(user2.reviews)
    print(user1.watched_movies)


def test_watchlist():
    # init watchlist
    watchlist = WatchList()
    print(f"Size of watchlist: {watchlist.size()}")

    # check_size
    watchlist = WatchList()
    print(f"Size of watchlist: {watchlist.size()}")

    # check_size_of_nonempty_watchlist
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")

    # check_add_movie
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")

    # check add_same_movie_again
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")

    # check_remove_movie_in_list
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.remove_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")

    # check_remove_movie_not_in_list
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")

    # check_select_movie_to_watch_index_ok
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(watchlist.select_movie_to_watch(2))

    # check_select_movie_to_watch_index_out_of_bounds
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.add_movie(Movie("Split", 2016))
    print(watchlist.select_movie_to_watch(4))

    # check_iterator_reaches_final_element
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.add_movie(Movie("Split", 2016))
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    for movie in watchlist:
        print(movie)
