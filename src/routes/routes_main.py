from os import chdir

import src.askers.askers_main as ask_main
from src.routes.routes_rename import rename_actionloop
from src.routes.routes_convert import convertloop
from src.utils import list_images_in_dir



def main_loop() -> None:
    print()
    dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
    if dir_main == "":
        return
    chdir(dir_main)

    while True:
        print()
        action = ask_main.ask_mainloop_action()
        print()
        if action == "list":
            list_images_in_dir()
            print()

        elif action == "change_dir":
            dir_main = ask_main.ask_path_filedialog("dir", "Choose images directory")
            if dir_main == "":
                return
            chdir(dir_main)

        elif action == "rename":
            print()
            outing = rename_actionloop()
            if not outing:
                return

        elif action =="convert":
            print()
            outing = convertloop()
            if not outing:
                return

        elif not action:
            return
