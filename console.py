#!/usr/bin/python3
""" define hbnb console"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
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
        args = arg.split()[0]

        if not args:
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
        elif args[0] not in self._classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

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
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[obj_key]
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
            for obj_key, obj in storage.all().items():
                objs.append(str(obj))
        print(objs)

    def default(self, arg):
        """default model"""
        arg_parts = arg.split('.')

        if len(arg_parts) != 2:
            print("*** Unknown syntax: {}".format(arg))
            return False

        cls_name, method_with_args = arg_parts

        if '(' not in method_with_args or ')' not in method_with_args:
            print("*** Unknown syntax: {}".format(arg))
            return False

        method, argx = method_with_args.split('(')
        argx = argx.split(')')[0]
        all_args = argx.split(',')

        argdict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }
        if method in argdict.keys():
            if method != "update":
                return argdict[method]("{} {}".format(cls_name, argx))
            else:
                obj_id = all_args[0]
                attr_name = all_args[1]
                attr_value = all_args[2]
                return argdict[method]("{} {} {} {}".format(
                    cls_name, obj_id, attr_name, attr_value))

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Count instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self._classes:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if type(obj).__name__ == args[0]:
                count += 1
        print(count)

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
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            dictionary = eval(' '.join(args[2:]))
            if not isinstance(dictionary, dict):
                raise ValueError
        except (NameError, ValueError):
            print("** invalid dictionary **")
            return
        obj = storage.all()[obj_key]
        for key, value in dictionary.items():
            setattr(obj, key, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
