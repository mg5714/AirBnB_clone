#!/usr/bin/python3
"""Defines unittests for state"""

import unittest
from unittest.mock import patch
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """unit test class"""

    def test_name_type(self):
        """Test that name is of type string"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_creation(self):
        """Test State instance creation"""
        state = State()
        self.assertIsInstance(state, State)

    def test_has_attribute(self):
        """Test that State has the correct attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_default_attribute_values(self):
        """Test default State attribute values"""
        state = State()
        self.assertEqual(state.name, "")

    @patch('models.state.BaseModel')
    def test_save_method(self, mock_base_model):
        """Test save method from BaseModel called when using State save"""
        state = State()
        state.save()
        self.assertFalse(mock_base_model.save.called)

    def test_to_dict_contains_correct_keys(self):
        """Test that the dictionary to_dict contains right keys"""
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_to_dict_contains_added_attribute(self):
        """Test that the dictionary returned by to_dict """
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["name"], "California")

    def test_str_representation(self):
        """Test the __str__ method has the correct format"""
        state = State()
        scn = state.__class__.__name__
        expected_format = f"[{scn}] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_format)

    def test_updated_at_sets_properly(self):
        """Test the updated_at after calling save"""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)

    def test_datetime_attributes(self):
        """Test that createdAt, updatedAt are datetime instances"""
        state = State()
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
