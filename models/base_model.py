#!/usr/bin/python3
import datetime
import uuid
import models


class BaseModel:
    """The base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        for k in kwargs:
            print("kwargs: {}: {}".format(k, kwargs[k]))

    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = str(dict_copy["created_at"])
        if ("updated_at" in dict_copy):
            dict_copy["updated_at"] = str(dict_copy["updated_at"])
        dict_copy["__class__"] = type(self).__name__
        return dict_copy