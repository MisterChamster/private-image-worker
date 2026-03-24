import os
from pathlib import Path
import pillow_heif

import src.askers.askers_renaming as ask_rnm
import src.renaming_tools as rnm_tools

pillow_heif.register_heif_opener()



def print_all_dates_loop(naming_style: str) -> str | None:
    gen = rnm_tools.check_single_image_dates(os.getcwd(), naming_style)
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

        elif action == "return":
            gen.close()
            return action

        elif not action:
            gen.close()
            return


def print_all_files_dates_loop(naming_style: str) -> str | None:
    while True:
        action = ask_rnm.ask_print_all_files_dates()
        print()

        if action == "date_time_original":
            rnm_tools.list_images_with_dates(os.getcwd(), "EXIF_DTO", naming_style)
            print()

        elif action == "date_time_digitized":
            rnm_tools.list_images_with_dates(os.getcwd(), "EXIF_DTD", naming_style)
            print()

        elif action == "date_time":
            rnm_tools.list_images_with_dates(os.getcwd(), "EXIF_DT", naming_style)
            print()

        elif action == "file_creation":
            rnm_tools.list_images_with_dates(os.getcwd(), "FILE_CREAT", naming_style)
            print()

        elif action == "file_modification":
            rnm_tools.list_images_with_dates(os.getcwd(), "FILE_MOD", naming_style)
            print()

        elif action == "return":
            return action

        elif not action:
            return


def rename_images_onebyone_loop(
    directory: str,
    naming_style: str
) -> str | None:
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir():
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            action = ask_rnm.ask_rename_images_one_by_one(image_path, naming_style)
            print()

            if action == "o":
                rnm_tools.rename_image_with_style(image_path, "EXIF_DTO", naming_style)
                print()

            elif action == "d":
                rnm_tools.rename_image_with_style(image_path, "EXIF_DTD", naming_style)
                print()

            elif action == "t":
                rnm_tools.rename_image_with_style(image_path, "EXIF_DT", naming_style)
                print()

            elif action == "c":
                rnm_tools.rename_image_with_style(image_path, "FILE_CREAT", naming_style)
                print()

            elif action == "m":
                rnm_tools.rename_image_with_style(image_path, "FILE_MOD", naming_style)
                print()

            elif action == "next":
                continue

            elif action == "rt":
                return action

            elif not action:
                return
    print("All files have been considered.\n")


def rename_all_images_loop(
    date_type: str,
    naming_style: str
) -> str | None:
    while True:
        action = ask_rnm.ask_rename_all_images(date_type)
        print()

        if action == "list_images_new_names":
            rnm_tools.list_images_with_dates(os.getcwd(), date_type, naming_style)
            print()

        elif action == "rename_all_images":
            rnm_tools.rename_images_in_dir(os.getcwd(), date_type, naming_style)
            print()

        elif action == "return":
            return action

        elif not action:
            return


def rename_basis_loop(naming_style: str) -> str | None:
    while True:
        action = ask_rnm.ask_rename_basis()
        print()

        if action == "date_time_original":
            outing = rename_all_images_loop("EXIF_DTO", naming_style)
            if not outing:
                return outing

        elif action == "date_time_digitized":
            outing = rename_all_images_loop("EXIF_DTD", naming_style)
            if not outing:
                return outing

        elif action == "date_time":
            outing = rename_all_images_loop("EXIF_DT", naming_style)
            if not outing:
                return outing

        elif action == "file_creation":
            outing = rename_all_images_loop("FILE_CREAT", naming_style)
            if not outing:
                return outing

        elif action == "file_modification":
            outing = rename_all_images_loop("FILE_MOD", naming_style)
            if not outing:
                return outing

        elif action == "return":
            return action

        elif not action:
            return


def rename_actionloop(dir_path: Path) -> str | None:
    # TEMPPPPPP
    os.chdir(dir_path)
    styles_dict = {
        "iso": "IMG_[Y][M][D]_[H][M][S]",
        "eu":  "IMG_[D][M][Y]_[H][M][S]",
        "us":  "IMG_[M][D][Y]_[H][M][S]"}
    naming_style = "iso"

    while True:
        print(f"Current naming style: {naming_style} {styles_dict[naming_style]}")
        action = ask_rnm.ask_rename_action()
        print()

        if action == "print_dates_first_file":
            outing = print_all_dates_loop(naming_style)
            if not outing:
                return

        elif action == "print_all_dates":
            outing = print_all_files_dates_loop(naming_style)
            if not outing:
                return

        elif action == "rename_one_by_one":
            outing = rename_images_onebyone_loop(os.getcwd(), naming_style)
            if not outing:
                return

        elif action == "rename_all_images":
            outing = rename_basis_loop(naming_style)
            if not outing:
                return

        elif action == "change_naming_style":
            outing = ask_rnm.ask_naming_style(naming_style)
            print()
            if not outing:
                return
            elif outing != "rt":
                naming_style = outing
                print()

        elif action == "return":
            return action

        elif not action:
            return
