#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the class for User
    Attributes:
        email: email address
        password: password for login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Relationships
    places = relationship(
            "Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship(
            "Review", cascade='all, delete, delete-orphan', backref="user")
