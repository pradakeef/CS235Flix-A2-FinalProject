from flask import Blueprint, render_template


search_blueprint = Blueprint('search_bp', __name__)


@search_blueprint.route('/search')
def search():
    return render_template(
        'search.html'
    )