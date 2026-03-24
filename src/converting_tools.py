import os
from pathlib import Path
from PIL import Image
import pillow_heif



def HEICtoPNG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            # create an Image object from the HEIC file
            print("Converting:", file_name)
            heif_file = pillow_heif.read_heif(file_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",)

            # create a new filename for the PNG file
            new_filename = os.path.splitext(file_name)[0] + ".png"
            new_filepath = os.path.join(images_dir, new_filename)

            image.save(new_filepath, format("png"))


def HEICtoPNG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            # create an Image object from the HEIC file
            filepath = os.path.join(images_dir, file_name)
            print("Converting:", file_name)
            try:
                heif_file = pillow_heif.read_heif(filepath)
            except ValueError:
                print(f"File {file_name} could not be coverted.")
                continue
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",)

            # create a new filename for the PNG file
            new_filename = os.path.splitext(file_name)[0] + ".png"
            new_filepath = os.path.join(images_dir, new_filename)
            try:
                os.remove(file_name)
            except:
                print("Couldn't remove " + file_name)

            image.save(new_filepath, format("png"))


def HEICtoJPG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            filepath = os.path.join(images_dir, file_name)
            new_filename = os.path.splitext(file_name)[0] + ".jpg"

            print("Converting:", file_name)
            img = Image.open(filepath)
            img.save(new_filename, format="JPEG")


def HEICtoJPG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            filepath = os.path.join(images_dir, file_name)
            new_filename = os.path.splitext(file_name)[0] + ".jpg"

            print("Converting:", file_name)
            img = Image.open(filepath)
            img.save(new_filename, format="JPEG")

            try:
                os.remove(file_name)
            except:
                print("Couldn't remove " + file_name)


def PNGtoJPG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".png":
            png_image = Image.open(file_name)
            print("Converting:", file_name)
            rgb_image = png_image.convert("RGB")
            new_filename = os.path.splitext(file_name)[0] + ".jpg"
            rgb_image.save(new_filename, "JPEG")


def PNGtoJPG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".png":
            png_image = Image.open(file_name)
            print("Converting:", file_name)
            rgb_image = png_image.convert("RGB")
            new_filename = os.path.splitext(file_name)[0] + ".jpg"
            rgb_image.save(new_filename, "JPEG")

            try:
                os.remove(file_name)
            except:
                print("Couldn't remove " + file_name)
