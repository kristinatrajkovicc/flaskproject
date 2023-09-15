from flask import Blueprint, render_template
from model.author import Author
from db import db

author_bp = Blueprint('author', __name__)

@author_bp.route('/authors')
def list_authors():
    authors = Author.query.all()
    return render_template('author/list.html', authors=authors)

@author_bp.route('/authors/<int:author_id>')
def author_details(author_id):
    author = Author.query.get(author_id)
    if author:
        return render_template('author/details.html', author=author)
    else:
        return "Autor nije pronađen", 404

