from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime
from pathlib import Path
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
            formatted_FILE_MOD_date   = get_formatted_name(image_path, "FILE_MOD")

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
            formatted_name = get_formatted_name(image_path, date_type)
            if formatted_name == "Invalid date":
                print(f"{formatted_name}:        {filename}")
                continue
            elif formatted_name == "No date":
                print(f"{formatted_name}:             {filename}")
                continue

            line_len = 80
            rest_len = len(f": {formatted_name}")
            if len(filename) > line_len + rest_len:
                filename = filename[:line_len + rest_len-3-4] + "..." + extension
            print(f"{formatted_name}: {filename}")


def rename_image(image_path, date_type):
    formatted_date_name = get_formatted_name(image_path, date_type)
    if formatted_date_name != "No date" and formatted_date_name != "Invalid date":
        dirname = os.path.dirname(image_path)
        for i in range(1, 200):
            new_filename = formatted_date_name + os.path.splitext(image_path)[1]
            new_filepath = dirname + "/" + new_filename
            os.path.normcase(new_filepath)
            try:
                print("HELLO OS.RENAME!")
                print(f"IMG PATH:      {image_path}\n" \
                      f"NEW FILE PATH: {new_filepath}")
                os.rename(image_path, new_filepath)
                og_filename = os.path.basename(image_path)
                print(f"Renamed: {og_filename} -> {new_filename}")
                return
            except FileExistsError:
                print(f"File {new_filename} already exists, trying with a different name.")
                formatted_date_name += f"_{i}"
                continue
        print("File name not changed. How the hell did you achieve this?")
    else:
        og_filename = os.path.basename(image_path)
        print(f"{og_filename} doesn't have a date of that type")


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
