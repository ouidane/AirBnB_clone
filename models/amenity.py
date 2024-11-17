#!/usr/bin/python3
"""Amenity Class module."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
