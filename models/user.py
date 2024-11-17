#!/usr/bin/python3
"""Module for the User Class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a user in the app.

    Attributes:
        email (str): The email address.
        password (str): The password.
        first_name (str): The first name.
        last_name (str): The last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
