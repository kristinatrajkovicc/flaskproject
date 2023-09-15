from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

