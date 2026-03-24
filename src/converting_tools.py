import os
from pathlib import Path
from PIL import Image
import pillow_heif

# TEMPPPPPP join del and not del

def HEICtoPNG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix

        # TEMPPPPPP reverse condition
        if ext.lower() == ".heic":
            # create an Image object from the HEIC file
            print("Converting:", file_name)
            heif_file = pillow_heif.read_heif(file_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",)

            new_filename = file_path.stem + ".png"
            new_filepath = images_dir / new_filename
            image.save(new_filepath, format("png"))


def HEICtoPNG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            # create an Image object from the HEIC file
            print("Converting:", file_name)
            try:
                heif_file = pillow_heif.read_heif(file_path)
            except ValueError:
                print(f"File {file_name} could not be coverted.")
                continue
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",)

            new_filename = file_path.stem + ".png"
            new_filepath = images_dir / new_filename
            image.save(new_filepath, format("png"))

            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_name)



def HEICtoJPG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            print("Converting:", file_name)
            # TEMPPPPPP put this in try block!!!
            img = Image.open(file_path)

            new_filename = file_path.stem + ".jpg"
            new_filepath = images_dir / new_filename
            img.save(new_filepath, format="JPEG")


def HEICtoJPG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".heic":
            print("Converting:", file_name)
            # TEMPPPPPP put this in try block!!!
            img = Image.open(file_path)

            new_filename = file_path.stem + ".jpg"
            new_filepath = images_dir / new_filename
            img.save(new_filepath, format="JPEG")

            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_name)


def PNGtoJPG_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".png":
            print("Converting:", file_name)
            # TEMPPPPPP put this in try block!!!
            png_image = Image.open(file_path)
            rgb_image = png_image.convert("RGB")

            new_filename = file_path.stem + ".jpg"
            new_filepath = images_dir / new_filename
            rgb_image.save(new_filepath, "JPEG")


def PNGtoJPG_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        # TEMPPPPPP
        images_dir = str(images_dir)
        file_name = file_path.name
        ext = file_path.suffix

        if ext.lower() == ".png":
            print("Converting:", file_name)
            # TEMPPPPPP put this in try block!!!
            png_image = Image.open(file_path)
            rgb_image = png_image.convert("RGB")

            new_filename = file_path.stem + ".jpg"
            new_filepath = images_dir / new_filename
            rgb_image.save(new_filepath, "JPEG")

            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_name)
