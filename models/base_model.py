#!/usr/bin/python3
""" Base model script """

import uuid
import datetime

class BaseModel:

    """ Class from which other classes inherit """

    def __init__(self, *args, **kwargs):
        """ initialize class object """
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        for k in kwargs:
            print("kwargs: {}: {}".format(k, kwargs[k]))

    def save(self):
        """ Update public instance property updated_at """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dict of all key/value of __dict__ """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict["created_at"].isoformat()
        obj_dict['updated_at'] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        """ Return official string representation """

        return "[{}] ({}) {}".\
        format(type(self).__name__, self.id, self.__dict__)
