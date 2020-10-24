from flask import Flask

import web_app.adapters.repository as repo
from web_app.adapters.memory_repository import MemoryRepository, populate


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')

    repo.repository_instance = MemoryRepository()
    populate('web_app/datafiles/Data1000Movies.csv', repo.repository_instance)

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app
