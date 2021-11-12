#!/usr/bin/python3
"""Console module - entry point of the command interpreter"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    # --- Advanced tasks --- (prec)
    def dict_update(self, arg):
        """updates an instance from a dictionary"""
        print("from dict update")
    def adv_parser(self, line):
        """Rearranges commands of syntax class.< command >()"""
        args0 = line.split(".")
        if len(args0) != 2:
            return line
        args1 = args0[1].split("(")
        if len(args1) == 2 and (args1[0] == "all" or args1[0] == "count"):
            if args1[1] == ")":
                self.onecmd(args1[0] + " " + args0[0])
            else:
                return line
        elif len(args1) == 2 and (args1[0] == "show" or args1[0] == "destroy"):
            args2 = args1[1].split("\"")
            if len(args2) == 3 and args2[2] == ")":
                self.onecmd(args1[0] + " " + args0[0] + " " + args2[1])
            elif len(args2) == 1 and args1[1] == ")":
                self.onecmd(args1[0] + " " + args0[0])
            else:
                return line
        elif len(args1) == 2 and args1[0] == "update":
            args2 = args1[1].split("\"")
            
            if len(args2) == 1 and args1[1] == ")":
                self.onecmd(args1[0] + " " + args0[0])
            elif len(args2) == 3 and args2[2] == ")":
                self.onecmd(args1[0] + " " + args0[0] + " " + args2[1])
            elif args2[-1] == "})" or args2[-1] == ", {})" or\
                 args2[-1] == ",{})" or args2[-1] == ", { })":
                self.dict_update(line)
            elif len(args2) == 5 and args2[4] == ")":
                self.onecmd(args1[0] + " " + args0[0] + " " + args2[1] + " " +
                     args2[3])
            elif len(args2) == 7 and args2[6] == ")":
                self.onecmd(args1[0] + " " + args0[0] + " " + args2[1] + " " +
                     args2[3] + " " + args2[5])
            else:
                print(args2[-1])
                return line
        else:
            return line

    def default(self, line):
        """Redirects input to adv_parser when syntax doesn't match"""
        response = self.adv_parser(line)
        if response == line:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """Retrieves the number of instances of a class
        Usage: <class name>.count()"""
        objs = storage.all()
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            instances = 0
            for id in objs.keys():
                classs = id.split(".")
                if arg == classs[0]:
                    instances += 1
            print(instances)

    # --- More functionality (console 0.1.0) ---
    def do_create(self, arg):
        """Creates a new instance of a class"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            base1 = storage.classes_dict()[arg]()
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
            if args[0] not in storage.classes_dict():
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

    def parse(self, arg):
        if arg == "" or arg is None:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in storage.classes_dict():
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id is missing **")
                return
            return args


if __name__ == "__main__":
    HBNBCommand().cmdloop()
