#!/usr/bin/python3
"""Defines unittests for city"""

import unittest
import os
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests covering all scenarios"""

    def test_city_instantiation(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_is_subclass(self):
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel))

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_id_is_str(self):
        city = City()
        self.assertIsInstance(city.id, str)

    def test_city_state_id_is_str(self):
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_name_is_str(self):
        city = City()
        self.assertIsInstance(city.name, str)

    def test_different_cities_have_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_city_created_updated_times(self):
        city = City()
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_city_name_assignment(self):
        city = City()
        name = "San Francisco"
        city.name = name
        self.assertEqual(city.name, name)

    def test_city_state_id_assignment(self):
        city = City()
        state_id = "CA"
        city.state_id = state_id
        self.assertEqual(city.state_id, state_id)

    def test_city_str_representation(self):
        city = City()
        city.id = "123456"
        expected_str = f"[City] (123456) {city.__dict__}"
        self.assertEqual(city.__str__(), expected_str)

    def test_city_empty_string_attributes(self):
        city = City(state_id="", name="")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        cityid = "City." + city.id
        with open("file.json", "r") as file:
            self.assertIn(cityid, file.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        city = City()
        city.middle_name = "Sudan"
        city.my_number = 249
        self.assertEqual("Sudan", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == '__main__':
    unittest.main()
