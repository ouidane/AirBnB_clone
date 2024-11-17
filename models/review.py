#!/usr/bin/python3
"""Module for the  Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in the HBnB application.

    Attributes:
        place_id (str): The identifier of the Place of the Review.
        user_id (str): The identifier of the User of the Review.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
