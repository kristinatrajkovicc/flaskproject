from flask import Flask
from flask_migrate import Migrate
import os

from blueprint import author_bp, book_bp, publisher_bp
from db import db

app = Flask(__name__)

migrate = Migrate(app, db)

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(author_bp, url_prefix='/author')
app.register_blueprint(book_bp, url_prefix='/book')
app.register_blueprint(publisher_bp, url_prefix='/publisher')










