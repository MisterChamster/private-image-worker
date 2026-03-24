from os import chdir

import src.askers.askers_main as ask_main
import src.routes.routes_rename as rnm_routes
import src.routes.routes_convert as cnv_routes
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
            exit_flag = rnm_routes.rename_actionloop(dir_main)
            if exit_flag:
                return

        elif action =="convert":
            print()
            outing = cnv_routes.convertloop(dir_main)
            if not outing:
                return

        elif action == "exit":
            return
