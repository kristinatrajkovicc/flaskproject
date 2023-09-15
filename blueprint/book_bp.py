from flask import Blueprint, render_template
from model.book import Book
from db import db

book_bp = Blueprint('book', __name__)

@book_bp.route('/books')
def list_books():
    books = Book.query.all()  # Promenite upit na odgovarajući model
    return render_template('book/list.html', books=books)