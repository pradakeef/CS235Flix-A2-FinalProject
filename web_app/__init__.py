from flask import Flask
from os.path import join as path_join

import web_app.adapters.repository as repo
from web_app.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')

    if test_config is None:
        data_path = path_join('CS235Flix', 'memory_repository')
    else:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repository_instance = MemoryRepository()
    populate('web_app/datafiles/Data1000Movies.csv', repo.repository_instance)

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .browsing import browse_by
        app.register_blueprint(browse_by.browse_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app
