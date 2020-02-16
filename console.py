#!/usr/bin/python3
"""module point 6 cmd class"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "
    __class_list = ["BaseModel"]

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of a class
        Usage: create <name of class>"""

        if not line:
            print("** class name missing **")
            return
        if line not in self.__class_list:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class> <id>"""
        args = shlex.split(line)
        largs = len(args)
        if largs < 1:
            print("** class name missing **")
        if largs == 1:
            if args[0] not in self.__class_list:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif largs == 2:
            models = storage.all()
            bm_key = "{}.{}".format(args[0], args[1])
            for key, value in models.items():
                if key == bm_key:
                    print(value)
                    return
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        Usage: $ all <class> or $ all"""
        models = storage.all()
        m_list = []
        if not line or line in self.__class_list:
            for key, value in models.items():
                m_list.append(str(value))
            print(m_list)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Usage: $ destroy <class> <id>"""
        args = shlex.split(line)
        largs = len(args)
        if largs < 1:
            print("** class name missing **")
        if largs == 1:
            if args[0] not in self.__class_list:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif largs == 2:
            models = storage.all()
            bm_key = "{}.{}".format(args[0], args[1])
            try:
                del models[bm_key]
                storage.save()
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
