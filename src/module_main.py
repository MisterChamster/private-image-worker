from .module_askers import ask_path, ask_mainloop_action
from .module_converter import convertloop
from .module_common import list_images_in_dir
from os import chdir



def mainloop():
    print()
    dir_main = ask_path()
    chdir(dir_main)

    while True:
        print()
        action = ask_mainloop_action()
        if action == "ls":
            list_images_in_dir()
            print()
        elif action == "cd":
            dir_main = ask_path()
            chdir(dir_main)
        elif action =="cnv":
            print()
            convertloop()
        elif action == "exit":
            break
