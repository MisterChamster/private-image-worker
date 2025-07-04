from os.path import exists
from .module_renamer import get_formatted_name
import os



# ========================== MAIN ==========================
def ask_mainloop_action():
    while True:
        print("Enter action: \n" \
        "ls   - List all images in folder.\n" \
        "cd   - Change program working directory.\n" \
        "rnm  - Rename...\n" \
        "cnv  - Convert...\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["ls", "cd", "rnm", "cnv", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path
        else:
            print("Invalid path.\n")


# ========================= CONVERT =========================
def ask_convert_action():
    while True:
        print("Enter convert action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "lsp  - List all .png files in folder\n" \
        "htp  - .heic to .png...\n" \
        "ptj  - .png to .jpg...\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["lsh", "htp", "lsp", "ptj", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_htp_action():
    while True:
        print("Enter heic to png action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "hpn  - Convert .heic files to .png files (leave heic files)\n" \
        "hpd  - Convert .heic files to .png files (delete heic files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["lsh", "hpn", "hpd", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_ptj_action():
    while True:
        print("Enter png to jpg action: \n" \
        "lsp  - List all .png files in folder\n" \
        "pjn  - Convert .png files to .jpg files (leave png files)\n" \
        "pjd  - Convert .png files to .jpg files (delete png files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["lsp", "pjn", "pjd", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


# ========================= RENAME =========================
def ask_rename_action():
    while True:
        print("Enter rename action: \n" \
        "pfd  - Print all dates of the first file in folder...\n" \
        "pad  - Print all images names converted to a date format...\n" \
        "roo  - Rename images names one by one...\n" \
        "rai  - Rename all images names to a date format...\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["pfd", "pad", "roo", "rai", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_print_all_dates():
    while True:
        print("Show next file dates?\n" \
        "Enter - Next.\n" \
        "rt    - Return.\n" \
        "exit  - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            if action == "":
                return "next"
            return action


def ask_print_all_files_dates():
    while True:
        print("What format to print?\n" \
        "dto  - DateTimeOriginal.\n" \
        "dtd  - DateTimeDigitized.\n" \
        "dt   - DateTime.\n" \
        "fc   - File creation.\n" \
        "fm   - File modification.\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["dto", "dtd", "dt", "fc", "fm", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_convert_dates_one_by_one(image_path):
    filename = os.path.basename(image_path)
    formatted_EXIF_DTO_date   = get_formatted_name(image_path, "EXIF_DTO")
    formatted_EXIF_DTD_date   = get_formatted_name(image_path, "EXIF_DTD")
    formatted_EXIF_DT_date    = get_formatted_name(image_path, "EXIF_DT")
    formatted_FILE_CREAT_date = get_formatted_name(image_path, "FILE_CREAT")
    formatted_FILE_MOD_date   = get_formatted_name(image_path, "FILE_MOD")
    while True:
        user_inputs = ["rt", "exit"]
        anything_flag = False
        print(f"Converting {filename}")
        if formatted_EXIF_DTO_date != "No date":
            user_inputs.append("o")
            anything_flag = True
            print(f"o - DateTimeOriginal EXIF:  {formatted_EXIF_DTO_date}")

        if formatted_EXIF_DTD_date != "No date":
            user_inputs.append("d")
            anything_flag = True
            print(f"d - DateTimeDigitized EXIF: {formatted_EXIF_DTD_date}")

        if formatted_EXIF_DT_date != "No date":
            user_inputs.append("t")
            anything_flag = True
            print(f"t - DateTime EXIF:          {formatted_EXIF_DT_date}")

        if formatted_FILE_CREAT_date != "No date":
            user_inputs.append("c")
            anything_flag = True
            print(f"c - File creation date:     {formatted_FILE_CREAT_date}")

        if formatted_FILE_MOD_date != "No date":
            user_inputs.append("m")
            anything_flag = True
            print(f"m - File modified date:     {formatted_FILE_MOD_date}")

        if anything_flag == False:
            print("No valid dates for this image. Skipping...")
            return "next"
        else:
            user_inputs.append("")
            print("Enter - Skip.")

        print("rt    - Return.\n" \
        "exit  - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in user_inputs:
            print("Incorrect input.\n")
        else:
            if action == "":
                return "next"
            return action


def ask_convert_all_dates_loop():
    while True:
        print("\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action not in ["rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action
