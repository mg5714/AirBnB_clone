#!/usr/bin/python3
"""Defines unittests for console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """class for testing"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))

    def test_eof_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("")
            self.assertEqual(output.getvalue(), "")

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("invalid_command"))
            self.assertIn(
                    "*** Unknown syntax: invalid_command",
                    output.getvalue().strip())

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("invalid_command"))
            self.assertIn(
                    "*** Unknown syntax: invalid_command",
                    output.getvalue().strip())

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("count BaseModel")

    def test_count_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("count InvalidClassName"))
            self.assertIn(
                    "** class doesn't exist **",
                    output.getvalue().strip())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            obj_id = fake_out.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = fake_out.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            obj_id = fake_out.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertNotIn(obj_id, storage.all().keys())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
