from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime
from pathlib import Path
from .module_askers import ask_rename_action,            \
                           ask_print_all_dates,          \
                           ask_print_all_files_dates,    \
                           ask_convert_dates_one_by_one, \
                           ask_convert_all_dates_loop
import pillow_heif
pillow_heif.register_heif_opener()



def get_image_date(image_path, date_type):
    """Extracts the date the image was taken from EXIF metadata."""
    #date_type can be strings: FILE_MOD, FILE_CREAT, EXIF_DTO, EXIF_DTD, EXIF_DT
    if date_type in ["EXIF_DTO", "EXIF_DTD", "EXIF_DT"]:
        try:
            with Image.open(image_path) as img:
                exif_data = img.getexif()
                if exif_data:
                    tag_dict = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}

                    if date_type == "EXIF_DTO":
                        try:
                            # print("PRONT DateTimeOriginal" + tag_dict.get("DateTimeOriginal"))
                            return tag_dict.get("DateTimeOriginal")
                        except:
                            return "No DateTimeOriginal EXIF"
                    elif date_type == "EXIF_DTD":
                        try:
                            # print("PRONT DateTimeDigitized" + tag_dict.get("DateTimeDigitized"))
                            return tag_dict.get("DateTimeDigitized")
                        except:
                            return "No DateTimeDigitized EXIF"
                    elif date_type == "EXIF_DT":
                        try:
                            # print("PRONT DateTime" + tag_dict.get("DateTime"))
                            return tag_dict.get("DateTime")
                        except:
                            return "No DateTime EXIF"
                else:
                    return "No EXIF data"
        except Exception as e:
            print(f"Error reading {image_path}: {e}")

    elif date_type in ["FILE_MOD", "FILE_CREAT"]:
        stats = Path(image_path).stat()
        if date_type == "FILE_CREAT":
            created = str(datetime.fromtimestamp(stats.st_birthtime))
            created = (":".join(created.split("-"))).split(".")[0]
            # print(created)
            return created
        elif date_type == "FILE_MOD":
            modified = str(datetime.fromtimestamp(stats.st_mtime))
            modified = ":".join(modified.split("-")).split(".")[0]
            # print(modified)
            return modified

    else:
        raise ValueError("module_renamer.py/get_image_date error: " \
        "Wrong input mr programmer.")


def format_date(date_string):
    """Formats %Y:%m:%d %H:%M:%S date as IMG_[Y][M][D]_[H][M][S]."""
    try:
        dt = datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
        return dt.strftime("IMG_%Y%m%d_%H%M%S")
    except ValueError:
        return "Invalid date"


def get_formatted_name(image_path, date_type):
    image_date = get_image_date(image_path, date_type)
    formatted_name   = format_date(image_date)            \
        if image_date != "No date" and                    \
            image_date is not None                        \
        else "No date"
    return formatted_name


def check_single_image_dates(directory):
    """Generator function listing images with all possible date types."""
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            formatted_EXIF_DTO_date   = get_formatted_name(image_path, "EXIF_DTO")
            formatted_EXIF_DTD_date   = get_formatted_name(image_path, "EXIF_DTD")
            formatted_EXIF_DT_date    = get_formatted_name(image_path, "EXIF_DT")
            formatted_FILE_CREAT_date = get_formatted_name(image_path, "FILE_CREAT")
            formatted_FILE_MOD_date = get_formatted_name(image_path, "FILE_MOD")

            yield filename + "\n" + \
                  "By DateTimeOriginal EXIF:  " + formatted_EXIF_DTO_date   + "\n" + \
                  "By DateTimeDigitized EXIF: " + formatted_EXIF_DTD_date   + "\n" + \
                  "By DateTime EXIF:          " + formatted_EXIF_DT_date    + "\n" + \
                  "By file creation:          " + formatted_FILE_CREAT_date + "\n" + \
                  "By file modification:      " + formatted_FILE_MOD_date   + "\n"


def list_images_with_dates(directory, date_type):
    """Lists all images in the directory with date_type dates in the format IMG_[Y][M][D]_[H][M][S]."""
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        extension = filename.lower().split(".")[-1]
        if extension in valid_extensions:
            image_path = os.path.join(directory, filename)
            date_created = get_image_date(image_path, date_type)
            formatted_date = format_date(date_created)   \
                if date_created != "No date" and         \
                   date_created is not None              \
                else "No date"

            line_len = 80
            rest_len = len(f": {formatted_date}")
            if len(filename) > line_len + rest_len:
                filename = filename[:line_len + rest_len-3-4] + "..." + extension
            print(f"{formatted_date}: {filename}")


def rename_images(directory, date_type):
    """Renames images in a directory based on their capture date."""
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            date_created = get_image_date(image_path, date_type)

            if date_created:
                #THIS WILL NEED WORK TOO
                formatted_date = format_date(date_created)
                if formatted_date:
                    new_filename = formatted_date + os.path.splitext(filename)[1]
                    for i in range(1, 100):
                        try:
                            new_path = os.path.join(directory, new_filename)
                            # print(f"Image: {image_path} -> New Path: {new_path}")
                            os.rename(image_path, new_path)
                            print(f"Renamed: {filename} -> {new_filename}")
                            break
                        except FileExistsError:
                            print(f"File {new_filename} already exists, trying with a number suffix.")
                            new_filename = new_filename.split('.')[0] + f"_{i}." + new_filename.split('.')[-1]
                            continue

                else:
                    print(f"Skipping {filename}: Invalid date format")
            else:
                print(f"Skipping {filename}: No date found")


# ========================= LOOPS =========================
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

            action = ask_convert_dates_one_by_one(filename)
            if action == "rt" or action == "exit":
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
