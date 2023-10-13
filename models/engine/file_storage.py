#!/usr/bin/python3
""" Class Filestorage module """

import datetime
import json
import os

class FileStorage:

    """ class for storing data """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets __objects """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dictionary = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(dictionary, f)

    def reload(self):
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




