#!/usr/bin/python3
"""Defines the State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a geographical state.

    Attributes:
        name (str): The name of the geographical state.
    """

    name = ""
