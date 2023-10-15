#!/usr/bin/python3
""" Unittests for FileStorage class """

import unittest
import models


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage_instantiation(unittest.TestCase):
    """ unittests for instantiation testing """
    def test_FileStorage_imstantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_path_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)