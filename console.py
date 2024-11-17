#!/usr/bin/python3
"""Defines the HBnB Console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parsing(arg):
    """Parse a string argument and return a list of items."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [item.strip(",") for item in split(arg)]
        else:
            main_pieces = split(arg[:brackets.span()[0]])
            rtn_list = [item.strip(",") for item in main_pieces]
            rtn_list.append(brackets.group())
            return rtn_list
    else:
        main_pieces = split(arg[:curly_braces.span()[0]])
        rtn_list = [item.strip(",") for item in main_pieces]
        rtn_list.append(curly_braces.group())
        return rtn_list


class HBNBCommand(cmd.Cmd):
    """HBnB command-line interface.

    Attributes:
        prompt (str): The prompt displayed in the command line.
        __classes (set): A set of model classes.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
        }

    def emptyline(self):
        """Do nothins when receiving an empty line."""
        pass

    def default(self, arg):
        """Handle unrecognized command.

        Args:
            arg (str): The unrecognized command.
        """
        default_args = {
            "all": self.do_all,
            "count": self.do_count,
            "destroy": self.do_destroy,
            "show": self.do_show,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in default_args.keys():
                    call = "{} {}".format(args[0], command[1])
                    return default_args[command[0]](call)
        print("** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command."""
        return True

    def do_EOF(self, arg):
        """EOF signal to."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance"""
        list_args = parsing(arg)
        if len(list_args) == 0:
            print("** class name missing **")
            return False
        if list_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        print(eval(list_args[0])().id)
        storage.save()

    def do_show(self, arg):
        """Display an instance of a given id as a string."""
        list_args = parsing(arg)
        objs = storage.all()
        if len(list_args) == 0:
            print("** class name missing **")
            return False
        if list_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(list_args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_args[0], list_args[1]) not in objs:
            print("** no instance found **")
            return False
        print(objs["{}.{}".format(list_args[0], list_args[1])])

    def do_destroy(self, arg):
        """Delete the instance of the given id."""
        list_args = parsing(arg)
        objs = storage.all()
        if len(list_args) == 0:
            print("** class name missing **")
            return False
        if list_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(list_args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_args[0], list_args[1]) not in objs:
            print("** no instance found **")
            return False
        del objs["{}.{}".format(list_args[0], list_args[1])]
        storage.save()

    def do_all(self, arg):
        """Display all instances of a given class as a string"""
        list_args = parsing(arg)
        if len(list_args) > 0 and list_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        list_objs = []
        if len(list_args) == 0:
            print([obj.__str__() for obj in storage.all().values()])
        elif len(list_args) > 0:
            for obj in storage.all().values():
                if list_args[0] == obj.__class__.__name__:
                    list_objs.append(obj.__str__())
            print(list_objs)

    def do_update(self, arg):
        """Update the instance of a given id."""
        list_args = parsing(arg)
        objs = storage.all()
        if len(list_args) == 0:
            print("** class name missing **")
            return False
        if list_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(list_args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_args[0], list_args[1]) not in objs:
            print("** no instance found **")
            return False
        if len(list_args) == 2:
            print("** attribute name missing **")
            return False
        if len(list_args) == 3:
            try:
                type(eval(list_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(list_args) == 4:
            obj = objs["{}.{}".format(list_args[0], list_args[1])]
            if list_args[2] in obj.__class__.__dict__.keys():
                type_val = type(obj.__class__.__dict__[list_args[2]])
                obj.__dict__[list_args[2]] = type_val(list_args[3])
            else:
                obj.__dict__[list_args[2]] = list_args[3]
        elif type(eval(list_args[2])) == dict:
            obj = objs["{}.{}".format(list_args[0], list_args[1])]
            for key, value in eval(list_args[2]).items():
                if (
                    key in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[key]) in [str, int, float]
                ):
                    type_val = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = type_val(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """Retrive the number of instances of a given class."""
        list_args = parsing(arg)
        count = 0
        for obj in storage.all().values():
            if list_args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
