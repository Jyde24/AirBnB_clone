#!/usr/bin/python3
from models import *

class Review(BaseModel):
    """A simple model to represent user reviews"""

    place_id = ""
    user_id = ""
    text = ""
