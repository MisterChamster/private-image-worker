import os
from pathlib import Path
import pillow_heif

import src.askers.askers_renaming as ask_rnm
import src.renaming_tools as rnm_tools

pillow_heif.register_heif_opener()



def print_all_dates_loop_cwd(
        dir_path: Path,
        naming_style: str
) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    gen = rnm_tools.check_single_image_dates(
        dir_path,
        naming_style)
    print(next(gen))

    while True:
        action = ask_rnm.ask_print_all_dates()
        print()

        if action == "next":
            try:
                print(next(gen))
            except:
                print("All pictures have been checked.\n")
                break

        elif action in exit_flags:
            gen.close()
            return exit_flags[action]


def print_all_files_dates_loop(
        dir_path: Path,
        naming_style: str
        ) -> bool:
    date_types = {
        "date_time_original": "EXIF_DTO",
        "date_time_digitized": "EXIF_DTD",
        "date_time": "EXIF_DT",
        "file_creation": "FILE_CREAT",
        "file_modification": "FILE_MOD"}
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_rnm.ask_print_all_files_dates()
        print()

        if action in date_types:
            rnm_tools.list_images_with_dates(
                dir_path,
                date_types[action],
                naming_style)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def rename_images_onebyone_loop(
    dir_path: Path,
    naming_style: str
) -> bool:
    date_types = {
        "date_time_original": "EXIF_DTO",
        "date_time_digitized": "EXIF_DTD",
        "date_time": "EXIF_DT",
        "file_creation": "FILE_CREAT",
        "file_modification": "FILE_MOD"}
    exit_flags = {
        "return": False,
        "exit": True}
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')

    for file_path in dir_path.iterdir():
        if file_path.suffix.lower() in valid_extensions:
            action = ask_rnm.ask_rename_images_one_by_one(file_path, naming_style)
            print()

            if action in date_types:
                rnm_tools.rename_image_with_style(
                    file_path,
                    date_types[action],
                    naming_style)
                print()

            elif action == "next":
                continue

            elif action in exit_flags:
                return exit_flags[action]
    print("All files have been considered.\n")


def rename_all_images_loop(
    dir_path: Path,
    date_type: str,
    naming_style: str
) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_rnm.ask_rename_all_images(date_type)
        print()

        if action == "list_images_new_names":
            rnm_tools.list_images_with_dates(dir_path, date_type, naming_style)
            print()

        elif action == "rename_all_images":
            rnm_tools.rename_images_in_dir(dir_path, date_type, naming_style)
            print()

        elif action in exit_flags:
            return exit_flags[action]


def rename_basis_loop(
        dir_path: Path,
        naming_style: str
        ) -> bool:
    date_types = {
        "date_time_original": "EXIF_DTO",
        "date_time_digitized": "EXIF_DTD",
        "date_time": "EXIF_DT",
        "file_creation": "FILE_CREAT",
        "file_modification": "FILE_MOD"}
    exit_flags = {
        "return": False,
        "exit": True}

    while True:
        action = ask_rnm.ask_rename_basis()
        print()

        if action in date_types:
            exit_flag = rename_all_images_loop(
                dir_path,
                date_types[action],
                naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action in exit_flags:
            return exit_flags[action]


def rename_actionloop(dir_path: Path) -> bool:
    exit_flags = {
        "return": False,
        "exit": True}
    styles_dict = {
        "iso": "IMG_[Y][M][D]_[H][M][S]",
        "eu":  "IMG_[D][M][Y]_[H][M][S]",
        "us":  "IMG_[M][D][Y]_[H][M][S]"}
    naming_style = "iso"

    # TEMPPPPPP
    os.chdir(dir_path)

    while True:
        print(f"Current naming style: {naming_style} {styles_dict[naming_style]}")
        action = ask_rnm.ask_rename_action()
        print()

        if action == "print_dates_first_file":
            exit_flag = print_all_dates_loop_cwd(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action == "print_all_dates":
            exit_flag = print_all_files_dates_loop(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action == "rename_one_by_one":
            exit_flag = rename_images_onebyone_loop(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action == "rename_all_images":
            exit_flag = rename_basis_loop(dir_path, naming_style)
            if exit_flag:
                return exit_flags["exit"]

        elif action == "change_naming_style":
            outing = ask_rnm.ask_naming_style(naming_style)
            print()
            if outing == "exit":
                return exit_flags["exit"]
            elif outing != "return":
                naming_style = outing
                print()

        elif action in exit_flags:
            return exit_flags[action]
