from . import form_command
import os
import sys

def main() -> None:
    os.execv(form_command[0], form_command + sys.argv[1:])
    exit(11)

if __name__ == "__main__":
    main()
