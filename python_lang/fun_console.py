#!/usr/bin/python3
""" Fun console """
import cmd
from sys import argv
from os import chmod


class FunConsole(cmd.Cmd):

    """ Command line interpreter class
    """
    prompt = "<>> "

    def do_create(self, arg):
        """Prepare python file
          Enter name after typing 'create'
          Leave out '.py'
          Do not worry about spaces
        """
        arg = arg + ".py"
        arg = arg.replace(' ', '_')
        sentence = "#!/usr/bin/python3\n"

        with open(arg, 'w') as f:
            f.write(sentence)
        chmod(arg, 0o744)

    def emptyline(self):
        pass

    def do_EOF(self, *args):
        """Exit the console """
        print("")
        print("Bye!")
        return True

    def do_quit(self, *args):
        """Exit the console """
        print("See ya!")
        return True

if __name__ == "__main__":
    FunConsole().cmdloop()
