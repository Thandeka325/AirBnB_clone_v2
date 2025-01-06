#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.first_name, (str, type(None))),
                (
                    "Expected type of first name to be str or NoneType, got "
                    f"{type(new.first_name)}"
                )
        )

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.last_name, (str, type(None))),
                (
                    "Expected type of last name to be str or NoneType, got "
                    f"{type(new.last_name)}"
                )
        )

    def test_email(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.email, (str, type(None))),
                (
                    "Expected type of email to be str or NoneType, got "
                    f"{type(new.email)}"
                )
        )

    def test_password(self):
        """ """
        new = self.value()
        self.assertTrue(
                isinstance(new.password, (str, type(None))),
                (
                    "Expected type of password to be str or NoneType, got "
                    f"{type(new.password)}"
                )
        )
