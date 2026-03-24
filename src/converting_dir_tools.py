import os
from pathlib import Path
from PIL import Image
import pillow_heif

import src.converting_file_tools as conv_file

# TEMPPPPPP join del and not del

def HEICtoPNG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        try:
            heif_file = pillow_heif.read_heif(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",)

        new_filename = file_path.stem + ".png"
        new_filepath = images_dir / new_filename
        image.save(new_filepath, format("png"))


def HEICtoPNG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        try:
            heif_file = pillow_heif.read_heif(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
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


def HEICtoJPG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        try:
            img = Image.open(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
        new_filename = file_path.stem + ".jpg"
        new_filepath = images_dir / new_filename
        img.save(new_filepath, format="JPEG")


def HEICtoJPG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        try:
            img = Image.open(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
        new_filename = file_path.stem + ".jpg"
        new_filepath = images_dir / new_filename
        img.save(new_filepath, format="JPEG")

        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_name)


def PNGtoJPG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".png":
            continue

        try:
            png_image = Image.open(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
        rgb_image = png_image.convert("RGB")
        new_filename = file_path.stem + ".jpg"
        new_filepath = images_dir / new_filename
        rgb_image.save(new_filepath, "JPEG")


def PNGtoJPG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        file_name = file_path.name
        ext = file_path.suffix
        if ext.lower() != ".png":
            continue

        try:
            png_image = Image.open(file_path)
        except ValueError:
            print(f"Can't open {file_name}")
            continue

        print("Converting:", file_name)
        rgb_image = png_image.convert("RGB")
        new_filename = file_path.stem + ".jpg"
        new_filepath = images_dir / new_filename
        rgb_image.save(new_filepath, "JPEG")

        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_name)
