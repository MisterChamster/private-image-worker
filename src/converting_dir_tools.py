import os
from pathlib import Path

import src.converting_file_tools as conv_file



def HEICtoPNG_dir(images_dir: Path, del_flag: bool = False) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoPNG(file_path)

        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)


def HEICtoJPG_dir(images_dir: Path, del_flag: bool = False) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".heic":
            continue

        conv_file.HEICtoJPG(file_path)

        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)


def PNGtoJPG_dir(images_dir: Path, del_flag: bool = False) -> None:
    for file_path in images_dir.iterdir():
        ext = file_path.suffix
        if ext.lower() != ".png":
            continue

        conv_file(file_path)

        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)
