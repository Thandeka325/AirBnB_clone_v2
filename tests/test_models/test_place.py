#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.city_id, (str, type(None))),
                (
                    "Expected type of city_id to be str or NoneType, got "
                    f"{type(new.city_id)}"
                )
        )

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.user_id, (str, type(None))),
                (
                    "Expected type of user_id to be str or NoneType, got "
                    f"{type(new.user_id)}"
                )
        )

    def test_name(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.name, (str, type(None))),
                (
                    "Expected type of name to be str or NoneType, got "
                    f"{type(new.name)}"
                )
        )

    def test_description(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.description, (str, type(None))),
                (
                    "Expected type of description to be str or NoneType, got "
                    f"{type(new.description)}"
                )
        )

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.number_rooms, (int, type(None))),
                (
                    "Expected type of number rooms to be int or NoneType, got "
                    f"{type(new.number_rooms)}"
                )
        )

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.number_bathrooms, (int, type(None))),
                (
                    "Expected type of number bathrooms\
                            to be int or NoneType, got "
                    f"{type(new.number_bathrooms)}"
                )
        )

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.max_guest, (int, type(None))),
                (
                    "Expected type of max guest to be int or NoneType, got "
                    f"{type(new.max_guest)}"
                )
        )

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.price_by_night, (int, type(None))),
                (
                    "Expected type of price by night\
                            to be int or NoneType, got "
                    f"{type(new.price_by_night)}"
                )
        )

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.latitude, (float, type(None))),
                (
                    "Expected type of latitude to be float or NoneType, got "
                    f"{type(new.latitude)}"
                )
        )

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.longitude, (float, type(None))),
                (
                    "Expected type of longitude to be float or NoneType, got "
                    f"{type(new.longitude)}"
                )
        )

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.amenity_ids, (list, type(None))),
                (
                    "Expected type of amenity ids to be list or NoneType, got "
                    f"{type(new.amenity_ids)}"
                )
        )
