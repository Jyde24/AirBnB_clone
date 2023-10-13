#!/usr/bin/python3
""" Base model script """

import uuid
from datetime import datetime
from models import storage

class BaseModel:

    """ Class from which other classes inherit """

    def __init__(self, *args, **kwargs):
        """ initialize class object

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value args"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def save(self):
        """ Update public instance property updated_at """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Return a dict of all key/value of __dict__ """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        """ Return official string representation """

        return "[{}] ({}) {}".\
        format(type(self).__name__, self.id, self.__dict__)
