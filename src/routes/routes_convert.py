from pathlib import Path

import src.utils as utils
import src.askers.askers_converting as ask_cnv
import src.converting_dir_tools as cnv



def htp_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htp_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(dir_path, "heic")
            print()

        elif action == "heic_to_png_no_del":
            cnv.HEICtoPNG_dir_no_del(dir_path)
            print()

        elif action == "heic_to_png_del":
            cnv.HEICtoPNG_dir_del(dir_path)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def htj_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htj_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(dir_path, "heic")
            print()

        elif action == "heic_to_jpg_no_del":
            cnv.HEICtoJPG_dir_no_del(dir_path)
            print()

        elif action == "heic_to_jpg_del":
            cnv.HEICtoJPG_dir_del(dir_path)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def ptj_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_ptj_action()
        print()

        if action == "list_png":
            utils.list_images_in_dir(dir_path, "png")
            print()

        elif action == "png_to_jpg_no_del":
            cnv.PNGtoJPG_dir_no_del(dir_path)
            print()

        elif action == "png_to_jpg_del":
            cnv.PNGtoJPG_dir_del(dir_path)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def convert_loop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_convert_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(dir_path, "heic")
            print()

        elif action == "list_png":
            utils.list_images_in_dir(dir_path, "png")
            print()

        elif action == "heic_to_png":
            print()
            exit_flag = htp_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "heic_to_jpg":
            print()
            exit_flag = htj_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "png_to_jpg":
            print()
            exit_flag = ptj_loop(dir_path)
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action in exit_flags:
            return exit_flags[action]
