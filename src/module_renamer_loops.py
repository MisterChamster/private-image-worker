import os
from .module_askers import ask_rename_action,            \
                           ask_print_all_dates,          \
                           ask_print_all_files_dates,    \
                           ask_rename_images_one_by_one, \
                           ask_rename_all_images_loop
from .module_renamer import check_single_image_dates,    \
                            list_images_with_dates,      \
                            rename_image
import pillow_heif
pillow_heif.register_heif_opener()



def printalldatesloop():
    gen = check_single_image_dates(os.getcwd())
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


def printallfilesdatesloop():
    while True:
        action = ask_print_all_files_dates()
        if action == "dto":
            list_images_with_dates(os.getcwd(), "EXIF_DTO")
            print()
        elif action == "dtd":
            list_images_with_dates(os.getcwd(), "EXIF_DTD")
            print()
        elif action == "dt":
            list_images_with_dates(os.getcwd(), "EXIF_DT")
            print()
        elif action == "fc":
            list_images_with_dates(os.getcwd(), "FILE_CREAT")
            print()
        elif action == "fm":
            list_images_with_dates(os.getcwd(), "FILE_MOD")
            print()
        elif action == "rt" or action == "exit":
            return action


def renameimagesonebyoneloop(directory):
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir():
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            action = ask_rename_images_one_by_one(image_path)

            if action == "o":
                rename_image(image_path, "EXIF_DTO")
                print()
            elif action == "d":
                rename_image(image_path, "EXIF_DTD")
                print()
            elif action == "t":
                rename_image(image_path, "EXIF_DT")
                print()
            elif action == "c":
                rename_image(image_path, "FILE_CREAT")
                print()
            elif action == "m":
                rename_image(image_path, "FILE_MOD")
                print()
            elif action == "next":
                continue
            elif action == "rt" or action == "exit":
                return action
    print("All files have been considered.\n")


def renameallimagesloop():
    while True:
        action = ask_rename_all_images_loop()
        if action == "rt" or action == "exit":
            return action


def renameloop():
    while True:
        action = ask_rename_action()

        if action == "pfd":
            outing = printalldatesloop()
            if outing == "exit":
                return outing
        elif action == "pad":
            outing = printallfilesdatesloop()
            if outing == "exit":
                return outing
        elif action == "roo":
            outing = renameimagesonebyoneloop(os.getcwd())
            if outing == "exit":
                return outing
        elif action == "rai":
            outing = renameallimagesloop()
            if outing == "exit":
                return outing
        elif action == "rt" or action == "exit":
            return action
