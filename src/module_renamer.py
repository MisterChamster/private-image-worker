from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime
from .module_askers import ask_rename_action
import pillow_heif
pillow_heif.register_heif_opener()



def get_image_date(image_path):
    """Extracts the date the image was taken from EXIF metadata."""
    try:
        with Image.open(image_path) as img:
            exif_data = img.getexif()

            # creation_time = os.path.getctime(image_path)
            # print(creation_time)
            # dt = datetime.fromtimestamp(creation_time)
            # return str(dt)

            if exif_data:
                tag_dict = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
                # Try to return the most reliable tag
                return (
                    #COME BACK HERE IF SOMETHING DOES NOT WORK
                    # tag_dict.get("DateTimeOriginal") or
                    tag_dict.get("DateTimeDigitized") or
                    tag_dict.get("DateTime") or
                    "No date"
                )
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
    return "No date"


def format_date(date_string):
    """Formats the date as IMG_[Y][M][D]_[H][M][S]."""
    try:
        dt = datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
        return dt.strftime("IMG_%Y%m%d_%H%M%S")
    except ValueError:
        return "Invalid date"


def list_images_with_dates(directory):
    """Lists all images in the directory with their capture dates in the format IMG_[Y][M][D]_[H][M][S]."""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            date_created = get_image_date(image_path)
            formatted_date = format_date(date_created) if date_created != "No date" else date_created
            print(f"{filename}: {formatted_date}")


def rename_images(directory):
    """Renames images in a directory based on their capture date."""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(directory, filename)
            date_created = get_image_date(image_path)
            
            if date_created:
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


def renameloop():
    while True:
        action = ask_rename_action()

        if action == "rt":
            return action
        elif action == "exit":
            return action
