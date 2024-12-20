#!/usr/bin/python3
"""City Class model."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The state id.
        name (str): The city name.
    """

    state_id = ""
    name = ""
