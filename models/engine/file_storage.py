#!/usr/bin/python3
"""Define the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Storage of objects as JSON.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary containing all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Set in __objects the obj with key."""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )] = obj

    def save(self) -> None:
        """Serialize __objects to the JSON file."""
        old_obj = FileStorage.__objects
        new_obj = {obj: old_obj[obj].to_dict() for obj in old_obj.keys()}
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(new_obj, fd)

    def reload(self) -> None:
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as fd:
                dict_obj = json.load(fd)
                for obj in dict_obj.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
