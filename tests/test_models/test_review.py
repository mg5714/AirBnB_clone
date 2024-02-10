#!/usr/bin/python3
"""Defines unittests for review """

import unittest
from unittest.mock import patch
import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """class unit test """

    def setUp(self):
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "321"
        self.review.text = "Great place!"

    def test_init(self):
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attributes_exist(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_default_attributes(self):
        new_review = Review()
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")

    def test_set_attributes(self):
        self.review.place_id = "new_place_id"
        self.review.user_id = "new_user_id"
        self.review.text = "New text"
        self.assertEqual(self.review.place_id, "new_place_id")
        self.assertEqual(self.review.user_id, "new_user_id")
        self.assertEqual(self.review.text, "New text")

    @patch('models.base_model.BaseModel.save')
    def test_save(self, mock_save):
        self.review.save()
        mock_save.assert_called_once()

    def test_to_dict_contains_correct_keys(self):
        self.review.save()  # to set updated_at
        review_dict = self.review.to_dict()
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("id", review_dict)

    def test_to_dict_contains_expected_values(self):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.review.save()
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["place_id"], self.review.place_id)
        self.assertEqual(review_dict["user_id"], self.review.user_id)
        self.assertEqual(review_dict["text"], self.review.text)
        self.assertEqual(review_dict["__class__"], "Review")
        created_at = self.review.created_at.strftime(time_format)
        self.assertEqual(review_dict["created_at"], created_at)
        updated_at = self.review.updated_at.strftime(time_format)
        self.assertEqual(review_dict["updated_at"], updated_at)


if __name__ == '__main__':
    unittest.main()
