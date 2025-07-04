import os
from .module_askers import ask_rename_action,            \
                           ask_print_all_dates,          \
                           ask_print_all_files_dates,    \
                           ask_convert_dates_one_by_one, \
                           ask_convert_all_dates_loop
from .module_renamer import check_single_image_dates,    \
                            list_images_with_dates
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


def convertdatesonebyoneloop(directory):
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir():
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            action = ask_convert_dates_one_by_one(image_path)

            if action == "o":
                pass
            elif action == "d":
                pass
            elif action == "t":
                pass
            elif action == "c":
                pass
            elif action == "m":
                pass
            elif action == "next":
                continue
            elif action == "rt" or action == "exit":
                return action
    print("All files have been considered.\n")


def convertalldatesloop():
    while True:
        action = ask_convert_all_dates_loop()
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
            outing = convertdatesonebyoneloop(os.getcwd())
            if outing == "exit":
                return outing
        elif action == "rai":
            outing = convertalldatesloop()
            if outing == "exit":
                return outing
        elif action == "rt" or action == "exit":
            return action
