import os
from pathlib import Path
from PIL import Image
import pillow_heif



def HEICtoPNG(image_path: Path) -> None:
    try:
        heif_file = pillow_heif.read_heif(image_path)
    except ValueError:
        print(f"Can't open {image_path}")

    print("Converting:", image_path.name)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",)

    new_filename = image_path.stem + ".png"
    new_filepath = image_path.parent / new_filename
    image.save(new_filepath, format("png"))


def HEICtoJPG(image_path: Path) -> None:
    try:
        img = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    new_filename = image_path.stem + ".jpg"
    new_filepath = image_path.parent / new_filename
    img.save(new_filepath, format="JPEG")


def PNGtoJPG(image_path: Path) -> None:
    try:
        png_image = Image.open(image_path)
    except ValueError:
        print(f"Can't open {image_path.name}")

    print("Converting:", image_path.name)
    rgb_image = png_image.convert("RGB")
    new_filename = image_path.stem + ".jpg"
    new_filepath = image_path.parent / new_filename
    rgb_image.save(new_filepath, "JPEG")
