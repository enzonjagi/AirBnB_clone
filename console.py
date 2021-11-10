#!/usr/bin/python3
"""Console module - entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    # --- More functionality (console 0.1.0) ---
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg != "basemodel":
            return False
        base1 = BaseModel()
        base1.save()
        print(base1.id)
        if not base1.__class__.__name__:
            print("** class doesn't exist **")
        elif base1.__class__.__name__ == "":
            print("** class name missing **")

    def do_show(self):
        """Prints the string representation of an instance"""
        pass

    def do_destroy(self):
        """Deletes an instance based on the class name and id"""
        pass

    def do_update(self):
        """Updates an instance based on the class name and id"""
        pass

    def do_all(self):
        """Prints all string representation of all instances"""
        pass

    # --- Basic functionality (console 0.0.1) ---
    def do_EOF(self, *arg):
        """Exits program at EOF"""
        print()
        return True

    def do_quit(self, *arg):
        """QUIT command that exits the program"""
        return True

    def emptyline(self):
        """Does nothing on an empty line + ENTER"""
        pass

    def precmd(self, line):
        line = line.lower()
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
