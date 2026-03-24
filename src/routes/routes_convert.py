import os
from pathlib import Path

import src.utils as utils
import src.askers.askers_converting as ask_cnv
import src.converting_tools as cnv



def htp_loop() -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htp_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(Path.cwd(), "heic")
            print()

        elif action == "heic_to_png_no_del":
            cnv.HEICtoPNG_no_del(os.getcwd())
            print()

        elif action == "heic_to_png_del":
            cnv.HEICtoPNG_del(os.getcwd())
            print()

        elif action in exit_flags:
            return exit_flags[action]


def htj_loop() -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_htj_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(Path.cwd(), "heic")
            print()

        elif action == "heic_to_jpg_no_del":
            cnv.HEICtoJPG_no_del(os.getcwd())
            print()

        elif action == "heic_to_jpg_del":
            cnv.HEICtoJPG_del(os.getcwd())
            print()

        elif action in exit_flags:
            return exit_flags[action]


def ptj_loop() -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_cnv.ask_ptj_action()
        print()

        if action == "list_png":
            utils.list_images_in_dir(Path.cwd(), "png")
            print()

        elif action == "png_to_jpg_no_del":
            cnv.PNGtoJPG_no_del(os.getcwd())
            print()

        elif action == "png_to_jpg_del":
            cnv.PNGtoJPG_del(os.getcwd())
            print()

        elif action in exit_flags:
            return exit_flags[action]


def convert_loop(dir_path: Path) -> str | None:
    exit_flags = {
        "return": False,
        "exit": True}

    # TEMPPPPPP
    os.chdir(dir_path)
    while True:
        action = ask_cnv.ask_convert_action()
        print()

        if action == "list_heic":
            utils.list_images_in_dir(Path.cwd(), "heic")
            print()

        elif action == "list_png":
            utils.list_images_in_dir(Path.cwd(), "png")
            print()

        elif action == "heic_to_png":
            print()
            exit_flag = htp_loop()
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "heic_to_jpg":
            print()
            exit_flag = htj_loop()
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action == "png_to_jpg":
            print()
            exit_flag = ptj_loop()
            if exit_flag:
                return exit_flags["exit"]
            print()

        elif action in exit_flags:
            return exit_flags[action]
