#!/usr/bin/python3
"""This the module for the Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""
    __tablename__ = "amenities"
    if storage_t == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
