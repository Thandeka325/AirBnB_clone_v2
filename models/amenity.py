#!/usr/bin/python3
"""This the module for the Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    if storage_t == "db":
        def get_place_amenity():
            from models.place import place_amenity
            return place_amenity

        places = relationship(
            "Place",
            secondary=get_place_amenity, back_populates="amenities"
        )
