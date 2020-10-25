import pytest
from web_app.browsing import services as browse
from web_app.authentication import services as auth
from datetime import datetime

def test_browse_by_get_movie_info(a_memory_repo):
    movie_info = browse.get_movie_info("Split", 2016, a_memory_repo)
    assert movie_info == {'title': "Split",
                'release_year': 2016,
                'description': "Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.",
                'director': "M. Night Shyamalan",
                'actors': ["James McAvoy", "Anya Taylor-Joy", "Haley Lu Richardson", "Jessica Sula"],
                'genres': ["Horror", "Thriller"],
                'runtime': 117}

def test_browse_by_get_non_existant_movie_info(a_memory_repo):
    assert browse.get_movie_info("Nope", 2016, a_memory_repo) is None

def test_get_number_per_genre(a_memory_repo, a_file_reader):
    data_from_test = dict()
    for movie in a_file_reader.dataset_of_movies:
        for item in movie.genres:
            if item.genre_name in data_from_test:
                data_from_test[item.genre_name] += 1
            else:
                data_from_test[item.genre_name] = 1
    for key, val in data_from_test.items():
        assert val == browse.get_pop_of_genre(key, a_memory_repo)

def test_add_user(a_memory_repo):
    auth.add_user('Billy', 'showmeThem0ney!', a_memory_repo)
    user_dict = auth.get_user('billy', a_memory_repo)
    assert user_dict['username'] == 'billy'

def test_authenticate_user(a_memory_repo):
    auth.add_user('Billy', 'showmeThem0ney!', a_memory_repo)
    assert auth.authenticate_user('billy', 'showmeThem0ney!', a_memory_repo) is True

def test_authenticate_non_existant_user(a_memory_repo):
    auth.add_user('Billy', 'showmeThem0ney!', a_memory_repo)
    assert auth.services.authenticate_user('john', 'showmeThem0ney!', a_memory_repo) is False

def test_authenticate_user_with_bad_password(a_memory_repo):
    auth.add_user('Billy', 'showmeThem0ney!', a_memory_repo)
    assert auth.authenticate_user('billy', 'showmetheMoney!', a_memory_repo) is False

