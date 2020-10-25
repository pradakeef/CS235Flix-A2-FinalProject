from web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

def test_csv_file():
    # check_file_reads_in
    filename = 'CS235Flix-A2-FinalProject/test/data/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    # check_length_of_movie_lists_are_accurate
    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

    # check_equality_sorting_movie_dataset_objects
    all_directors_sorted = sorted(movie_file_reader.dataset_of_directors)
    print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')

    all_actors_sorted = sorted(movie_file_reader.dataset_of_actors)
    print(f'first 3 unique directors of sorted dataset: {all_actors_sorted[0:3]}')

    all_movies_sorted = sorted(movie_file_reader.dataset_of_movies)
    print(f'first 3 unique directors of sorted dataset: {all_movies_sorted[0:3]}')

    # check_movie_attributes_are_accessible
    for movie in all_movies_sorted[0:3]:
        print(f"Movie: {movie}")
        print(f"Movie Description: {movie.description}")
        print(f"Movie Actors: {movie.actors}")
        print(f"Movie Rating: {movie.external_rating}")

def test_read():
    test = MovieFileCSVReader('CS235Flix\\memory_repository\\Data1000Movies.csv')
    test.read_csv_file()

    assert len(test.dataset_of_movies) == 1000
    assert len(test.dataset_of_actors) == 1985
    assert len(test.dataset_of_directors) == 644
    assert len(test.dataset_of_genres) == 20
