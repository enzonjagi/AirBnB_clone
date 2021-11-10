#!/usr/bin/python3
"""Console module - entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

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
