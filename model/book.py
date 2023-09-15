from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', backref='books')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"



