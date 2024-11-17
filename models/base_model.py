#!/usr/bin/python3
"""Define the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project.

    Attributes:
        id (str): A unique identifier generated using the uuid4() function.
        created_at (datetime): The date & time when
            the instance is created.
        updated_at (datetime): The date & time when
            the instance is last updated.

    Methods:
        __init__: Initializes a new instance of the BaseModel class.
        __str__: Returns a string representation of the BaseModel instance.
        save: Updates the 'updated_at' attribute and saves the instance.
        to_dict: Returns a dictionary representation of the BaseModel instance.
    """

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
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """Update the 'updated_at' attribute and save the instance."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self) -> dict:
        """Return a dictionary representation of the BaseModel instance."""
        rtn_dict = self.__dict__.copy()
        rtn_dict["created_at"] = self.created_at.isoformat()
        rtn_dict["updated_at"] = self.updated_at.isoformat()
        rtn_dict["__class__"] = self.__class__.__name__
        return rtn_dict
