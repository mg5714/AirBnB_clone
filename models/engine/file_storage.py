#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """filestorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        fo = FileStorage.__objects
        serialized_objects = {}

        for key, value in fo.items():
            if hasattr(value, 'to_dict') and callable(
                    getattr(value, 'to_dict')):
                serialized_objects[key] = value.to_dict()
            else:
                serialized_objects[key] = value

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        class_ = eval(class_name)
                        obj = class_(**value)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass


storage = FileStorage()
storage.reload()
