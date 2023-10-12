""" Defines unittests for models/base_model.py """

import unittest
from datetime import datetime
from models.base_model  import BaseModel

class Test_BaseModel(unittest.TestCase):
    """
    Test base model class
    """

    def setUp(self):
        self.model1 = BaseModel()

        args = {'created_at': datetime(2017, 2, 10, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 10, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(args)

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)

if __name__ == '__main__':
    unittest.main()

