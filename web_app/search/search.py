from flask import Blueprint, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField

import web_app.adapters.repository as repo
import web_app.search.services as services

search_blueprint = Blueprint('search_bp', __name__)

class SearchForm(FlaskForm):
    search_string = StringField('Search Text')
    genre_radio_buttons = SelectField('Genre', choices=[''] + [genre.genre_name for genre in repo.repository_instance.get_genres()])
    actor_checkbox = BooleanField('Actor')
    title_checkbox = BooleanField('Title', default='checked')
    director_checkbox = BooleanField('Director')
    submit = SubmitField('Search')

@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST':
        movie_list = services.search_movies(form.search_string.data.lower(), form.genre_radio_buttons.data, form.title_checkbox.data,
                                            form.actor_checkbox.data, form.director_checkbox.data, repo.repository_instance)
        return render_template('search.html', handler_url=url_for('search_bp.search'), form=form, movies=movie_list)
    return render_template('search.html', handler_url=url_for('search_bp.search'), form=form)
