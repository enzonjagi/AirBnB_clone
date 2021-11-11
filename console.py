#!/usr/bin/python3
"""Console module - entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    # --- More functionality (console 0.1.0) ---
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            base1 = storage.classes()[arg]()
            base1.save()
            print(base1.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on class name and id"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        for id in objs.keys():
            if id == args[0] + "." + args[1]:
                print(objs[id])
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        for id in objs.keys():
            if id == args[0] + "." + args[1]:
                del objs[id]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        objs = storage.all()
        args = self.parse(arg)
        if args is None:
            return
        elif args[0] + "." + args[1] not in objs.keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            for id in objs.keys():
                if id == args[0] + "." + args[1]:
                    setattr(objs[id], str(args[2]), args[3])
                    objs[id].save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = storage.all()
        objs_list = []
        if arg != "" and arg is not None:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                for id in objs.keys():
                    if objs[id].__class__.__name__ == args[0]:
                        objs_list.append(objs[id].__str__())
        else:
            for id in objs.keys():
                objs_list.append(objs[id].__str__())
        if len(objs_list) > 0:
            print(objs_list)

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
        return line

    def parse(self, arg):
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id is missing **")
                return
            return args


if __name__ == "__main__":
    HBNBCommand().cmdloop()
