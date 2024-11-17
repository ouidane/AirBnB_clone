#!/usr/bin/python3
"""Module for the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represents a Place in the HBnB application.

    Attributes:
        city_id (str): City identifier.
        user_id (str): User identifier.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Room count in the place.
        number_bathrooms (int): Bathroom count in the place.
        max_guest (int): Maximum guest capacity.
        price_by_night (int): Cost per night.
        latitude (float): Geographic latitude.
        longitude (float): Geographic longitude.
        amenity_ids (list): List of amenity identifiers.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
