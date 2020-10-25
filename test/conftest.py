import pytest
from os.path import join as path_join
import web_app.adapters.repository as repo
from web_app.adapters.memory_repository import MemoryRepository, populate
from web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from web_app import create_app

TEST_DATA_PATH = path_join('test', 'data')

@pytest.fixture
def a_memory_repo():
    repo.repository_instance = MemoryRepository()
    populate(TEST_DATA_PATH, repo.repository_instance)
    return repo.repository_instance

@pytest.fixture
def a_file_reader():
    reader = MovieFileCSVReader(path_join(TEST_DATA_PATH, 'Data1000Movies.csv'))
    reader.read_csv_file()
    return reader

@pytest.fixture
def client():
    test_app = create_app({
        'TESTING': True, 'TEST_DATA_PATH': TEST_DATA_PATH, 'WTF_CSRF_ENABLED': False})
    return test_app.test_client()

class TheUser:
    def __init__(self, client):
        self.__client = client

    def login(self, username='pradakeef', password='mAgicprada123'):
        return self.__client.post('/login', data={'username': username, 'password': password})

    def logout(self):
        return self.__client.get('/logout')

@pytest.fixture
def user_credential(client):
    return TheUser(client)
