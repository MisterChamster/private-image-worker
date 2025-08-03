from src.askers.common import ask_path, ask_mainloop_action
from src.renamer_loops import rename_actionloop
from src.converter_loops import convertloop
from src.utils import list_images_in_dir
from os import chdir



def main_loop():
    print()
    dir_main = ask_path()
    if dir_main == "exit":
        return
    chdir(dir_main)

    while True:
        print()
        action = ask_mainloop_action()
        if action == "ls":
            list_images_in_dir()
            print()
        elif action == "cd":
            dir_main = ask_path()
            if dir_main == "exit":
                return
            chdir(dir_main)
        elif action == "rnm":
            print()
            outing = rename_actionloop()
            if outing == "exit":
                return
        elif action =="cnv":
            print()
            outing = convertloop()
            if outing == "exit":
                return
        elif action == "exit":
            return
