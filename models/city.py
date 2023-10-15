#!/usr/bin/python3

from models import *

class City(BaseModel):
    """Simple model to represent the city in a state"""

    state_id = ""
    name = ""
