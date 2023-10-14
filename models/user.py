#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    """ A model representation of user fields"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
