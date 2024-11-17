#!/usr/bin/python3
"""Defines Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in the HBnB application.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
