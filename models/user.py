#!/usr/bin/python3
"""Defines the User Class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user in the HBnB application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
