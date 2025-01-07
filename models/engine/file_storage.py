#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from importlib import import_module
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        If cls is provided, it filters by cls type.
        """
        if cls is None:
            return self.__objects
        else:
            return {
                key: val for key, val in self.__objects.items()
                if isinstance(val, cls)
            }

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
            {f"{obj.__class__.__name__}.{obj.id}": obj}
        )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as file:
            temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    self.__objects[key] = self.model_classes[cls_name](**val)

    def close(self):
        """Closes the storage engine by reloading the JSON file."""
        self.reload()
