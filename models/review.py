#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """A simple model to represent user reviews"""

    place_id = ""
    user_id = ""
    text = ""
