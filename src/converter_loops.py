import os
from src.utils import list_images_in_dir
from src.askers.converting import (ask_convert_action,
                                   ask_htp_action,
                                   ask_htj_action,
                                   ask_ptj_action)
from src.converter import (HEICtoPNG_no_del,
                           HEICtoPNG_del,
                           HEICtoJPG_no_del,
                           HEICtoJPG_del,
                           PNGtoJPG_no_del,
                           PNGtoJPG_del)



def htploop():
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
            return None


def htjloop():
    while True:
        action = ask_htj_action()

        if action == "lsh":
            list_images_in_dir("heic")
            print()
        elif action == "hjn":
            HEICtoJPG_no_del(os.getcwd())
            print()
        elif action == "hjd":
            HEICtoJPG_del(os.getcwd())
            print()
        elif action == "rt":
            return action
        elif action == None:
            return None


def ptjloop():
    while True:
        action = ask_ptj_action()

        if action == "lsp":
            list_images_in_dir("png")
            print()
        elif action == "pjn":
            PNGtoJPG_no_del(os.getcwd())
            print()
        elif action == "pjd":
            PNGtoJPG_del(os.getcwd())
            print()
        elif action == "rt":
            return action
        elif action == None:
            return None


def convertloop():
    while True:
        action = ask_convert_action()

        if action == "lsh":
            list_images_in_dir("heic")
            print()
        elif action == "lsp":
            list_images_in_dir("png")
            print()
        elif action == "htp":
            print()
            outing = htploop()
            if outing == None:
                return None
            print()
        elif action == "htj":
            print()
            outing = htjloop()
            if outing == None:
                return None
            print()
        elif action == "ptj":
            print()
            outing = ptjloop()
            if outing == None:
                return None
            print()
        elif action == "rt":
            return action
        elif action == None:
            return None
