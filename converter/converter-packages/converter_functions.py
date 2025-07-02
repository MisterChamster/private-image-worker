import os
from PIL import Image
import pillow_heif



def HEICtoPNG_no_del(directory):
    # heic to png no deletion
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
    # heic to png deletion
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


def PNGtoJPG_del(directory):
    # png to jpg deletion
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
                