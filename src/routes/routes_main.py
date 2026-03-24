from os import chdir

import src.askers.askers_main as ask_main
from src.routes.routes_rename import rename_actionloop
from src.routes.routes_convert import convertloop
import src.utils as utils



def main_loop() -> None:
    print()
    dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
    if not dir_main:
        return

    while True:
        print()
        action = ask_main.ask_mainloop_action()
        print()
        if action == "list":
            utils.list_images_in_dir(dir_main)
            print()

        elif action == "change_dir":
            dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
            if not dir_main:
                return

        elif action == "rename":
            print()
            outing = rename_actionloop(dir_main)
            if not outing:
                return

        elif action =="convert":
            print()
            outing = convertloop(dir_main)
            if not outing:
                return

        elif action == "exit":
            return
