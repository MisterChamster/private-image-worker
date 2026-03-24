import os
from pathlib import Path
from typing import Literal

import src.renaming_tools as rnm_tools



def ask_print_all_dates() -> Literal[
    "next",
    "return",
    "exit"]:
    returns_dict = {
        "":   "next",
        "rt": "return",
        "e":  "exit"}

    while True:
        print("Show next file dates?\n"
              "Enter - Next\n"
              "rt    - Return\n"
              "e     - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_print_all_files_dates() -> Literal[
    "date_time_original",
    "date_time_digitized",
    "date_time",
    "file_creation",
    "file_modification",
    "return",
    "exit"]:
    returns_dict = {
        "o":  "date_time_original",
        "d":  "date_time_digitized",
        "t":  "date_time",
        "c":  "file_creation",
        "m":  "file_modification",
        "rt": "return",
        "e":  "exit"}

    while True:
        print("Choose printing format:\n"
              "o  - DateTimeOriginal\n"
              "d  - DateTimeDigitized\n"
              "t  - DateTime\n"
              "c  - File creation\n"
              "m  - File modification\n"
              "rt - Return\n"
              "e  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_rename_images_one_by_one(
    image_path: str,
    naming_style: str
) -> str | None:
    returns_dict = {"rt": "return"}

    filename = os.path.basename(image_path)
    # TEMPPPPPP
    formatted_EXIF_DTO_date   = rnm_tools.get_formatted_name(Path(image_path), "EXIF_DTO", naming_style)
    formatted_EXIF_DTD_date   = rnm_tools.get_formatted_name(Path(image_path), "EXIF_DTD", naming_style)
    formatted_EXIF_DT_date    = rnm_tools.get_formatted_name(Path(image_path), "EXIF_DT", naming_style)
    formatted_FILE_CREAT_date = rnm_tools.get_formatted_name(Path(image_path), "FILE_CREAT", naming_style)
    formatted_FILE_MOD_date   = rnm_tools.get_formatted_name(Path(image_path), "FILE_MOD", naming_style)

    while True:
        anything_flag = False
        print(f"Renaming: {filename}")
        print("Choose renaming style:")
        if formatted_EXIF_DTO_date != "No date" and \
           formatted_EXIF_DTO_date != "Invalid date":
            returns_dict["o"] = "date_time_original"
            anything_flag = True
            print(f"o     - DateTimeOriginal EXIF:  {formatted_EXIF_DTO_date}")

        if formatted_EXIF_DTD_date != "No date" and \
           formatted_EXIF_DTD_date != "Invalid date":
            returns_dict["d"] = "date_time_digitized"
            anything_flag = True
            print(f"d     - DateTimeDigitized EXIF: {formatted_EXIF_DTD_date}")

        if formatted_EXIF_DT_date != "No date" and \
           formatted_EXIF_DT_date != "Invalid date":
            returns_dict["t"] = "date_time"
            anything_flag = True
            print(f"t     - DateTime EXIF:          {formatted_EXIF_DT_date}")

        if formatted_FILE_CREAT_date != "No date" and \
           formatted_FILE_CREAT_date != "Invalid date":
            returns_dict["c"] = "file_creation"
            anything_flag = True
            print(f"c     - File creation date:     {formatted_FILE_CREAT_date}")

        if formatted_FILE_MOD_date != "No date" and \
           formatted_FILE_MOD_date != "Invalid date":
            returns_dict["m"] = "file_modification"
            anything_flag = True
            print(f"m     - File modified date:     {formatted_FILE_MOD_date}")

        if anything_flag == False:
            print("No valid dates for this image. Skipping...")
            return "next"
        else:
            returns_dict[""] = "next"
            print("Enter - Skip")

        print("rt    - Return\n"
              "exit  - Exit program\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return
        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_rename_all_images(date_type: str) -> Literal[
    "list_images_new_names",
    "rename_all_images",
    "return",
    "exit"]:
    returns_dict = {
        "ls": "list_images_new_names",
        "ra": "rename_all_images",
        "rt": "return",
        "e":  "exit"}

    while True:
        print("Choose a renaming option:\n"
             f"ls - List all images names converted to {date_type} format\n"
             f"ra - Rename all images to {date_type} format\n"
              "rt - Return\n"
              "e  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_rename_basis() -> Literal[
    "date_time_original",
    "date_time_digitized",
    "date_time",
    "file_creation",
    "file_modification",
    "return",
    "exit"]:
    returns_dict = {
        "o": "date_time_original",
        "d": "date_time_digitized",
        "t": "date_time",
        "c": "file_creation",
        "m": "file_modification",
        "r": "return",
        "e":  "exit"}

    while True:
        print("Choose style of renaming images:\n"
              "o - DateTimeOriginal\n"
              "d - DateTimeDigitized\n"
              "t - DateTime\n"
              "c - File creation\n"
              "m - File modification\n"
              "r - Return\n"
              "e - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_rename_action() -> Literal[
    "print_dates_first_file",
    "print_all_dates",
    "rename_one_by_one",
    "rename_all_images",
    "change_naming_style",
    "return",
    "exit"]:
    returns_dict = {
        "pfd": "print_dates_first_file",
        "pad": "print_all_dates",
        "roo": "rename_one_by_one",
        "rai": "rename_all_images",
        "cns": "change_naming_style",
        "rt":  "return",
        "e":   "exit"}

    while True:
        print("Choose rename action:\n"
              "pfd - Print all dates of the first file in folder...\n"
              "pad - Print all images names converted to a date format...\n"
              "roo - Rename images one by one...\n"
              "rai - Rename all images to a date format...\n"
              "cns - Change naming style...\n"
              "rt  - Return\n"
              "e   - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_naming_style(naming_style: str) -> Literal[
    "iso",
    "eu",
    "us",
    "return",
    "exit"]:
    returns_dict = {
        "i": "iso",
        "e": "eu",
        "u": "us",
        "r": "return",
        "e": "exit"}

    while True:
        print(f"Current naming style: {naming_style}\n"
               "Choose naming style:\n"
               "i - ISO 8601  IMG_[Y][M][D]_[H][M][S]\n"
               "e - European  IMG_[D][M][Y]_[H][M][S]\n"
               "u - US Format IMG_[M][D][Y]_[H][M][S]\n"
               "r - Return\n"
               "e - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")
