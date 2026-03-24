import os
from pathlib import Path

import src.converting_file_tools as conv_file



def HEICtoPNG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoPNG(file_path)


def HEICtoPNG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoPNG(file_path)

        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def HEICtoJPG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoJPG(file_path)


def HEICtoJPG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoJPG(file_path)

        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)


def PNGtoJPG_dir_no_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".png":
            continue

        conv_file(file_path)


def PNGtoJPG_dir_del(images_dir: Path) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".png":
            continue

        conv_file(file_path)

        try:
            os.remove(file_path)
        except:
            print("Couldn't remove " + file_path.name)
