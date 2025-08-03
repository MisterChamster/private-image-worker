import os
from .askers import (ask_rename_action,
                     ask_print_all_dates,
                     ask_print_all_files_dates,
                     ask_rename_images_one_by_one,
                     ask_rename_style,
                     ask_rename_all_images)
from .renamer import (check_single_image_dates,
                      list_images_with_dates,
                      rename_image_with_style,
                      rename_images_in_dir)
import pillow_heif
pillow_heif.register_heif_opener()



def print_all_dates_loop(naming_style):
    gen = check_single_image_dates(os.getcwd(), naming_style)
    print(next(gen))
    while True:
        action = ask_print_all_dates()

        if action == "next":
            try:
                print(next(gen))
            except:
                print("All pictures have been checked.\n")
                break
        elif action == "rt" or action == "exit":
            gen.close()
            return action


def print_all_files_dates_loop(naming_style):
    while True:
        action = ask_print_all_files_dates()
        if action == "o":
            list_images_with_dates(os.getcwd(), "EXIF_DTO", naming_style)
            print()
        elif action == "d":
            list_images_with_dates(os.getcwd(), "EXIF_DTD", naming_style)
            print()
        elif action == "t":
            list_images_with_dates(os.getcwd(), "EXIF_DT", naming_style)
            print()
        elif action == "c":
            list_images_with_dates(os.getcwd(), "FILE_CREAT", naming_style)
            print()
        elif action == "m":
            list_images_with_dates(os.getcwd(), "FILE_MOD", naming_style)
            print()
        elif action == "rt" or action == "exit":
            return action


def rename_images_onebyone_loop(directory, naming_style):
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir():
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            action = ask_rename_images_one_by_one(image_path, naming_style)

            if action == "o":
                rename_image_with_style(image_path, "EXIF_DTO", naming_style)
                print()
            elif action == "d":
                rename_image_with_style(image_path, "EXIF_DTD", naming_style)
                print()
            elif action == "t":
                rename_image_with_style(image_path, "EXIF_DT", naming_style)
                print()
            elif action == "c":
                rename_image_with_style(image_path, "FILE_CREAT", naming_style)
                print()
            elif action == "m":
                rename_image_with_style(image_path, "FILE_MOD", naming_style)
                print()
            elif action == "next":
                continue
            elif action == "rt" or action == "exit":
                return action
    print("All files have been considered.\n")


def rename_all_images_loop(date_type, naming_style):
    while True:
        action = ask_rename_all_images(date_type)
        if action == "ls":
            list_images_with_dates(os.getcwd(), date_type, naming_style)
            print()
        elif action == "ren":
            rename_images_in_dir(os.getcwd(), date_type)
            print()
        elif action == "rt" or action == "exit":
            return action


def rename_basis_loop(naming_style):
    while True:
        action = ask_rename_style()
        if action == "o":
            outing = rename_all_images_loop("EXIF_DTO", naming_style)
            if outing == "exit":
                return outing
        elif action == "d":
            outing = rename_all_images_loop("EXIF_DTD", naming_style)
            if outing == "exit":
                return outing
        elif action == "t":
            outing = rename_all_images_loop("EXIF_DT", naming_style)
            if outing == "exit":
                return outing
        elif action == "c":
            outing = rename_all_images_loop("FILE_CREAT", naming_style)
            if outing == "exit":
                return outing
        elif action == "m":
            outing = rename_all_images_loop("FILE_MOD", naming_style)
            if outing == "exit":
                return outing
        elif action == "rt" or action == "exit":
            return action


def change_naming_style_loop(naming_style):
    return None


def rename_actionloop():
    naming_style = "IMG_[Y][M][D]_[H][M][S]"
    while True:
        print(f"Current naming style: {naming_style}")
        action = ask_rename_action()

        if action == "pfd":
            outing = print_all_dates_loop(naming_style)
            if outing == "exit":
                return outing
        elif action == "pad":
            outing = print_all_files_dates_loop(naming_style)
            if outing == "exit":
                return outing
        elif action == "roo":
            outing = rename_images_onebyone_loop(os.getcwd(), naming_style)
            if outing == "exit":
                return outing
        elif action == "rai":
            outing = rename_basis_loop(naming_style)
            if outing == "exit":
                return outing
        elif action == "cns":
            outing = change_naming_style_loop(naming_style)
            if outing == "exit":
                return outing
        elif action == "rt" or action == "exit":
            return action
