#!/usr/bin/python3
"""Defines unittests for place """


import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """unit test for palcemodel"""

    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attribute_types(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_default_attribute_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_setting_attributes(self):
        self.place.city_id = "1234abcd"
        self.place.user_id = "5678efgh"
        self.place.name = "My Lovely Place"
        self.place.description = "A place with a view"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 200
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["pool", "wifi", "gym"]

        self.assertEqual(self.place.city_id, "1234abcd")
        self.assertEqual(self.place.user_id, "5678efgh")
        self.assertEqual(self.place.name, "My Lovely Place")
        self.assertEqual(self.place.description, "A place with a view")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 200)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["pool", "wifi", "gym"])

    def test_attribute_edge_cases(self):
        self.place.number_rooms = -1
        self.place.number_bathrooms = -1
        self.place.max_guest = -1
        self.place.price_by_night = -1
        self.place.latitude = -200.0
        self.place.longitude = -200.0

        self.assertEqual(self.place.number_rooms, -1)
        self.assertEqual(self.place.number_bathrooms, -1)
        self.assertEqual(self.place.max_guest, -1)
        self.assertEqual(self.place.price_by_night, -1)
        self.assertEqual(self.place.latitude, -200.0)
        self.assertEqual(self.place.longitude, -200.0)


if __name__ == '__main__':
    unittest.main()
