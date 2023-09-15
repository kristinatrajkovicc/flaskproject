from flask import Blueprint, render_template
from model.publisher import Publisher  # Promenite import na odgovarajući model za izdavače
from db import db  # Promenite import na odgovarajući db objekat

publisher_bp = Blueprint('publisher', __name__)

@publisher_bp.route('/publishers')
def list_publishers():
    publishers = Publisher.query.all()  # Promenite upit na odgovarajući model
    return render_template('publisher/list.html', publishers=publishers)
