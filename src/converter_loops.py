import os
from .common import list_images_in_dir
from .askers import (ask_convert_action,
                     ask_htp_action,
                     ask_ptj_action)
from .converter import (HEICtoPNG_no_del,
                        HEICtoPNG_del,
                        PNGtoJPG_no_del,
                        PNGtoJPG_del)



def htploop():
    while True:
        action = ask_htp_action()

        if action == "lsh":
            list_images_in_dir("heic")
            print()
        elif action == "hpn":
            HEICtoPNG_no_del(os.getcwd())
            print()
        elif action == "hpd":
            HEICtoPNG_del(os.getcwd())
            print()
        elif action == "rt" or action == "exit":
            return action


def htjloop():
    print("Im coooonvertooooooong!")
    return


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
        elif action == "rt" or action == "exit":
            return action


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
            if outing == "exit":
                return outing
            print()
        elif action == "htj":
            print()
            outing = htjloop()
            if outing == "exit":
                return outing
            print()
        elif action == "ptj":
            print()
            outing = ptjloop()
            if outing == "exit":
                return outing
            print()
        elif action == "rt" or action == "exit":
            return action
