#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Set up test environment"""
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str(self):
        """Test string representation method"""
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        """Test save method"""
        my_model = BaseModel()

        old_updated_at = my_model.updated_at
        curr_updated_at = my_model.save()
        self.assertNotEqual(old_updated_at, curr_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()

        obj_dict = my_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('id' in obj_dict)
        self.assertEqual(obj_dict['id'], my_model.id)

if __name__ == '__main__':
    unittest.main()
