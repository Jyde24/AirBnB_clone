#!/usr/bin/python3
import json
from datetime import datetime
from models import *


class FileStorage:
    """
    This class is responsible for managing the storage and retrieval of objects in a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes a new FileStorage instance and loads objects from the JSON file if available.
        """
        self.reload()

    def all(self):
        """
        Returns a dictionary of all stored objects.

        Returns:
        dict: A dictionary of objects with their IDs as keys.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
        obj: An object to be stored.
        """
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        Saves the objects in the storage dictionary to the JSON file.
        """
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        """
        Reloads stored objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass









