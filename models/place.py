#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
import models

# Many-to-Many relationship table for Amenity and Place
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: price for a stay in int
        latitude: latitude in float
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # DBStorage relationship with Amenity
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="places"
        )
    else:
        @property
        def amenities(self):
            """Returns list of amenity ids"""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if review[0] == 'Amenity':
                    lista.append(var[key])
            for elem in lista:
                if elem.id in self.amenity_ids:
                    result.append(elem)
            return result

        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
