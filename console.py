#!/usr/bin/python3
""" define hbnb console"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.Place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """define console class"""
    prompt = "(hbnb) "
    _classes = ["BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            storage.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self._classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        print(storage.all()[args[0]][obj_key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self._classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        del storage.all()[args[0]][obj_key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of all instances."""
        args = arg.split()
        objs = []
        if not args:
            for obj_class in storage.all():
                for obj_key, obj in storage.all()[obj_class].items():
                    objs.append(str(obj))
        else:
            if args[0] not in self._classes:
                print("** class doesn't exist **")
                return
            for obj_key, obj in storage.all()[args[0]].items():
                objs.append(str(obj))
        print(objs)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self._classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[args[0]][obj_key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
