#!/usr/bin/python3
"""module point 6 cmd class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
