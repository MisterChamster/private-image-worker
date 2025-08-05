import os
from src.askers.renaming import (ask_rename_action,
                                 ask_print_all_dates,
                                 ask_print_all_files_dates,
                                 ask_rename_images_one_by_one,
                                 ask_rename_basis,
                                 ask_naming_style,
                                 ask_rename_all_images)
from src.renamer import (check_single_image_dates,
                         list_images_with_dates,
                         rename_image_with_style,
                         rename_images_in_dir)
import pillow_heif



pillow_heif.register_heif_opener()


def print_all_dates_loop(naming_style: str):
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
        elif action == "return":
            gen.close()
            return action
        elif action == None:
            gen.close()
            return None


def print_all_files_dates_loop(naming_style: str):
    while True:
        action = ask_print_all_files_dates()
        if action == "date_time_original":
            list_images_with_dates(os.getcwd(), "EXIF_DTO", naming_style)
            print()
        elif action == "date_time_digitized":
            list_images_with_dates(os.getcwd(), "EXIF_DTD", naming_style)
            print()
        elif action == "date_time":
            list_images_with_dates(os.getcwd(), "EXIF_DT", naming_style)
            print()
        elif action == "file_creation":
            list_images_with_dates(os.getcwd(), "FILE_CREAT", naming_style)
            print()
        elif action == "file_modification":
            list_images_with_dates(os.getcwd(), "FILE_MOD", naming_style)
            print()
        elif action == "return":
            return action
        elif action == None:
            return None


def rename_images_onebyone_loop(directory: str, naming_style: str):
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
            elif action == "rt":
                return action
            elif action == None:
                return None
    print("All files have been considered.\n")


def rename_all_images_loop(date_type: str, naming_style: str):
    while True:
        action = ask_rename_all_images(date_type)
        if action == "list_images_new_names":
            list_images_with_dates(os.getcwd(), date_type, naming_style)
            print()
        elif action == "rename_all_images":
            rename_images_in_dir(os.getcwd(), date_type, naming_style)
            print()
        elif action == "return":
            return action
        elif action == None:
            return None


def rename_basis_loop(naming_style: str):
    while True:
        action = ask_rename_basis()
        if action == "date_time_original":
            outing = rename_all_images_loop("EXIF_DTO", naming_style)
            if outing == None:
                return outing
        elif action == "date_time_digitized":
            outing = rename_all_images_loop("EXIF_DTD", naming_style)
            if outing == None:
                return outing
        elif action == "date_time":
            outing = rename_all_images_loop("EXIF_DT", naming_style)
            if outing == None:
                return outing
        elif action == "file_creation":
            outing = rename_all_images_loop("FILE_CREAT", naming_style)
            if outing == None:
                return outing
        elif action == "file_modification":
            outing = rename_all_images_loop("FILE_MOD", naming_style)
            if outing == None:
                return outing
        elif action == "return":
            return action
        elif action == None:
            return None


def rename_actionloop():
    naming_style = "iso"
    while True:
        print(f"Current naming style: {naming_style}")
        action = ask_rename_action()

        if action == "print_dates_first_file":
            outing = print_all_dates_loop(naming_style)
            if outing == None:
                return None
        elif action == "print_all_dates":
            outing = print_all_files_dates_loop(naming_style)
            if outing == None:
                return None
        elif action == "rename_one_by_one":
            outing = rename_images_onebyone_loop(os.getcwd(), naming_style)
            if outing == None:
                return None
        elif action == "rename_all_images":
            outing = rename_basis_loop(naming_style)
            if outing == None:
                return None
        elif action == "change_naming_style":
            outing = ask_naming_style(naming_style)
            if outing == None:
                return None
            elif outing != "rt":
                naming_style = outing
                print()
        elif action == "return":
            return action
        elif action == None:
            return None
