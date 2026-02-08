import os
from src.utils import list_images_in_dir
from src.askers.askers_converting import (ask_convert_action,
                                   ask_htp_action,
                                   ask_htj_action,
                                   ask_ptj_action)
from src.converter import (HEICtoPNG_no_del,
                           HEICtoPNG_del,
                           HEICtoJPG_no_del,
                           HEICtoJPG_del,
                           PNGtoJPG_no_del,
                           PNGtoJPG_del)



def htploop() -> str | None:
    while True:
        action = ask_htp_action()

        if action == "list_heic":
            list_images_in_dir("heic")
            print()

        elif action == "heic_to_png_no_del":
            HEICtoPNG_no_del(os.getcwd())
            print()

        elif action == "heic_to_png_del":
            HEICtoPNG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif action == None:
            return


def htjloop() -> str | None:
    while True:
        action = ask_htj_action()

        if action == "list_heic":
            list_images_in_dir("heic")
            print()

        elif action == "heic_to_jpg_no_del":
            HEICtoJPG_no_del(os.getcwd())
            print()

        elif action == "heic_to_jpg_del":
            HEICtoJPG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif action == None:
            return


def ptjloop() -> str | None:
    while True:
        action = ask_ptj_action()

        if action == "list_png":
            list_images_in_dir("png")
            print()

        elif action == "png_to_jpg_no_del":
            PNGtoJPG_no_del(os.getcwd())
            print()

        elif action == "png_to_jpg_del":
            PNGtoJPG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif action == None:
            return


def convertloop() -> str | None:
    while True:
        action = ask_convert_action()

        if action == "list_heic":
            list_images_in_dir("heic")
            print()

        elif action == "list_png":
            list_images_in_dir("png")
            print()

        elif action == "heic_to_png":
            print()
            outing = htploop()
            if outing == None:
                return
            print()

        elif action == "heic_to_jpg":
            print()
            outing = htjloop()
            if outing == None:
                return
            print()

        elif action == "png_to_jpg":
            print()
            outing = ptjloop()
            if outing == None:
                return
            print()

        elif action == "return":
            return action

        elif action == None:
            return
