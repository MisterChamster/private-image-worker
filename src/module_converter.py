import os
from PIL import Image
import pillow_heif
from .module_common import list_images_in_dir
from .module_askers import ask_convert_action



def HEICtoPNG_no_del(directory):
    for filename in os.listdir(directory):
        # check if the file is in HEIC format
        if filename.lower().endswith(".heic"):
            # create an Image object from the HEIC file
            filepath = os.path.join(directory, filename)
            print("Converting:", filename)
            heif_file = pillow_heif.read_heif(filepath)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )

            # create a new filename for the PNG file
            new_filename = os.path.splitext(filename)[0] + ".png"
            new_filepath = os.path.join(directory, new_filename)

            image.save(new_filepath, format("png"))


def HEICtoPNG_del(directory):
    for filename in os.listdir(directory):
        # check if the file is in HEIC format
        if filename.lower().endswith(".heic"):
            # create an Image object from the HEIC file
            filepath = os.path.join(directory, filename)
            print("Converting:", filename)
            heif_file = pillow_heif.read_heif(filepath)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )

            # create a new filename for the PNG file
            new_filename = os.path.splitext(filename)[0] + ".png"
            new_filepath = os.path.join(directory, new_filename)
            try:
                os.remove(filename)
            except:
                print("Couldn't remove " + filename)

            image.save(new_filepath, format("png"))


def PNGtoJPG_no_del(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_image = Image.open(filename)
            print("Converting:", filename)
            rgb_image = png_image.convert("RGB")
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            rgb_image.save(new_filename, "JPEG")


def PNGtoJPG_del(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_image = Image.open(filename)
            print("Converting:", filename)
            rgb_image = png_image.convert("RGB")
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            rgb_image.save(new_filename, "JPEG")

            try:
                os.remove(filename)
            except:
                print("Couldn't remove " + filename)

def convertloop():
    while True:
        action = ask_convert_action()

        if action == "lsh":
            list_images_in_dir("heic")
            print()
        elif action == "htp":
            pass
        elif action == "lsp":
            list_images_in_dir("png")
            print()
        elif action == "ptj":
            pass
        elif action == "rt":
            return
