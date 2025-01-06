#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.place_id, (str, type(None))),
                (
                    "Expected type of place id to be str or NoneType, got "
                    f"{type(new.place_id)}"
                )
        )

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.user_id, (str, type(None))),
                (
                    "Expected type of user id to be str or NoneType, got "
                    f"{type(new.user_id)}"
                )
        )

    def test_text(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.text, (str, type(None))),
                (
                    "Expected type of text to be str or NoneType, got "
                    f"{type(new.text)}"
                )
        )
