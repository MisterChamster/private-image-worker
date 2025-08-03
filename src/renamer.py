from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime
from pathlib import Path
import pillow_heif
pillow_heif.register_heif_opener()



def get_image_date(image_path: str, date_type: str):
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


def format_date(date_string: str, naming_style: str):
    """Formats %Y:%m:%d %H:%M:%S according to naming_style."""
    try:
        dt = datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
        if naming_style == "iso":
            return dt.strftime("IMG_%Y%m%d_%H%M%S")
        elif naming_style == "eu":
            return dt.strftime("IMG_%d%m%Y_%H%M%S")
        elif naming_style == "us":
            return dt.strftime("IMG_%m%d%Y_%H%M%S")
    except ValueError:
        return "Invalid date"


def get_formatted_name(image_path: str, date_type: str, naming_style: str):
    image_date = get_image_date(image_path, date_type)

    formatted_name = ""
    if image_date != "No date" and image_date is not None:
        formatted_name = format_date(image_date, naming_style)
    else:
        formatted_name = "No date"

    return formatted_name


def check_single_image_dates(directory: str, naming_style: str):
    """Generator function listing images with all possible date types."""
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            formatted_EXIF_DTO_date   = get_formatted_name(image_path, "EXIF_DTO", naming_style)
            formatted_EXIF_DTD_date   = get_formatted_name(image_path, "EXIF_DTD", naming_style)
            formatted_EXIF_DT_date    = get_formatted_name(image_path, "EXIF_DT", naming_style)
            formatted_FILE_CREAT_date = get_formatted_name(image_path, "FILE_CREAT", naming_style)
            formatted_FILE_MOD_date   = get_formatted_name(image_path, "FILE_MOD", naming_style)

            yield filename + "\n" + \
                  "By DateTimeOriginal EXIF:  " + formatted_EXIF_DTO_date   + "\n" + \
                  "By DateTimeDigitized EXIF: " + formatted_EXIF_DTD_date   + "\n" + \
                  "By DateTime EXIF:          " + formatted_EXIF_DT_date    + "\n" + \
                  "By file creation:          " + formatted_FILE_CREAT_date + "\n" + \
                  "By file modification:      " + formatted_FILE_MOD_date   + "\n"


def list_images_with_dates(directory: str, date_type: str, naming_style: str):
    """Lists all images in the directory with date_type dates with the appropriate naming style."""
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        extension = filename.lower().split(".")[-1]
        if extension in valid_extensions:
            image_path = os.path.join(directory, filename)
            formatted_name = get_formatted_name(image_path, date_type, naming_style)
            if formatted_name == "Invalid date":
                print(f"Invalid date:        {filename}")
                continue
            elif formatted_name == "No date":
                print(f"No date:             {filename}")
                continue

            line_len = 80
            rest_len = len(f": {formatted_name}")
            if len(filename) > line_len + rest_len:
                filename = filename[:line_len + rest_len-3-4] + "..." + extension
            print(f"{formatted_name}: {filename}")


def rename_image_with_style(image_path: str, date_type: str, naming_style: str):
    formatted_date_name = get_formatted_name(image_path, date_type, naming_style)
    if formatted_date_name != "No date" and formatted_date_name != "Invalid date":
        dirname = os.path.dirname(image_path)
        for i in range(1, 200):
            new_filename = formatted_date_name + os.path.splitext(image_path)[1]
            new_filepath = dirname + "/" + new_filename
            os.path.normcase(new_filepath)
            try:
                os.rename(image_path, new_filepath)
                og_filename = os.path.basename(image_path)
                print(f"Renamed:  {new_filename} <- {og_filename}")
                return
            except FileExistsError:
                print(f"File {new_filename} already exists, trying with a different name.")
                formatted_date_name += f"_{i}"
                continue
        print("File name not changed. How the hell did you achieve this?")
    elif formatted_date_name == "No date":
        og_filename = os.path.basename(image_path)
        print(f"{og_filename}: No {date_type} type date.")
    elif formatted_date_name == "Invalid date":
        og_filename = os.path.basename(image_path)
        print(f"{og_filename}: {date_type} date type is invalid.")


def rename_images_in_dir(directory: str, date_type: str, naming_style: str):
    valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')

    for filename in os.listdir(directory):
        extension = filename.lower().split(".")[-1]
        if extension in valid_extensions:
            image_path = os.path.join(directory, filename)
            rename_image_with_style(image_path, date_type, naming_style)
