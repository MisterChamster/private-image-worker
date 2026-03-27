import os
from pathlib import Path

import src.converting_file_tools as conv_file
import src.utils as utils



def HEICtoPNG_dir(images_dir: Path, del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".heic")

    for file_path in files_list:
        conv_file.HEICtoPNG(file_path)
        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)


def HEICtoJPG_dir(images_dir: Path, del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".heic")

    for file_path in files_list:
        conv_file.HEICtoJPG(file_path)
        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)


def PNGtoJPG_dir(images_dir: Path, del_flag: bool = False) -> None:
    files_list = utils.get_files_list(images_dir, ".png")

    for file_path in files_list:
        conv_file.PNGtoJPG(file_path)
        if del_flag:
            try:
                os.remove(file_path)
            except:
                print("Couldn't remove " + file_path.name)
