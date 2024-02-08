#!/usr/bin/python3

import os
import json
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Reset FileStorage before each test."""
        FileStorage._FileStorage__objects = {}
        
    @classmethod
    def tearDownClass(cls):
        """Clean up files created during tests."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open(FileStorage._FileStorage__file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            self.assertIn(key, data)

    def test_reload_no_file(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        storage = FileStorage()
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_reload_with_data(self):
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open(FileStorage._FileStorage__file_path, 'w', encoding="utf-8") as file:
            json.dump({obj_key: obj.to_dict()}, file)
        storage = FileStorage()
        storage.reload()
        self.assertIn(obj_key, storage.all())

    def test_reload_corrupted_data(self):
        corrupted_content = '{"corrupted}'
        with open(FileStorage._FileStorage__file_path, 'w', encoding="utf-8") as file:
            file.write(corrupted_content)
        storage = FileStorage()
        with self.assertRaises(Exception):
            storage.reload()

    def test_reload_with_mock(self):
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        fake_file_data = {obj_key: obj.to_dict()}

        m = mock_open(read_data=json.dumps(fake_file_data))
        with patch('models.file_storage.open', m, create=True):
            storage = FileStorage()
            storage.reload()
            self.assertIn(obj_key, storage.all())

if __name__ == '__main__':
    unittest.main()
