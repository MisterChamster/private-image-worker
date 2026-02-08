import os

from src.utils import list_images_in_dir
import src.askers.askers_converting as ask_cnv
import src.converting_tools as cnv



def htploop() -> str | None:
    while True:
        action = ask_cnv.ask_htp_action()
        print()

        if action == "list_heic":
            list_images_in_dir("heic")
            print()

        elif action == "heic_to_png_no_del":
            cnv.HEICtoPNG_no_del(os.getcwd())
            print()

        elif action == "heic_to_png_del":
            cnv.HEICtoPNG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif not action:
            return


def htjloop() -> str | None:
    while True:
        action = ask_cnv.ask_htj_action()
        print()

        if action == "list_heic":
            list_images_in_dir("heic")
            print()

        elif action == "heic_to_jpg_no_del":
            cnv.HEICtoJPG_no_del(os.getcwd())
            print()

        elif action == "heic_to_jpg_del":
            cnv.HEICtoJPG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif not action:
            return


def ptjloop() -> str | None:
    while True:
        action = ask_cnv.ask_ptj_action()
        print()

        if action == "list_png":
            list_images_in_dir("png")
            print()

        elif action == "png_to_jpg_no_del":
            cnv.PNGtoJPG_no_del(os.getcwd())
            print()

        elif action == "png_to_jpg_del":
            cnv.PNGtoJPG_del(os.getcwd())
            print()

        elif action == "return":
            return action

        elif not action:
            return


def convertloop() -> str | None:
    while True:
        action = ask_cnv.ask_convert_action()
        print()

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

        elif not action:
            return
