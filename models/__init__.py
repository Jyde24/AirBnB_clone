#!/usr/bin/python3
""" Initialise package """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
