#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """A class that represents the BaseModel of the HBnB app."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Not Used.
            **kwargs: Arbitrary keyword arguments.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f"
                        )
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Return the BaseModel instance as a string."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """Update and save the instance."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self) -> dict:
        """Return the BaseModel instance dictionary."""
        rtn_dict = self.__dict__.copy()
        rtn_dict["created_at"] = self.created_at.isoformat()
        rtn_dict["updated_at"] = self.updated_at.isoformat()
        rtn_dict["__class__"] = self.__class__.__name__
        return rtn_dict
