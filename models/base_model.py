#!/usr/bin/python3
""" Base model script """

import uuid
from datetime import datetime

class Basemodel:

    """ Class from which other classes inherit """

    def __init__(self):

        """ Initialize instance attributes

        Args:
            - * args: list of arguments
            - **kwargs: dict of key-value arguments
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
