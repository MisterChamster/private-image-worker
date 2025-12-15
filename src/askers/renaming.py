from src.renamer import get_formatted_name
import os



def ask_print_all_dates():
    returns_dict = {"": "next",
                    "rt": "return"}

    while True:
        print("Show next file dates?\n" \
        "Enter - Next.\n"               \
        "rt    - Return.\n"             \
        "exit  - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_print_all_files_dates():
    returns_dict = {"o": "date_time_original",
                    "d": "date_time_digitized",
                    "t": "date_time",
                    "c": "file_creation",
                    "m": "file_modification",
                    "rt": "return"}

    while True:
        print("Choose printing format:\n"          \
        "o    - DateTimeOriginal.\n"               \
        "d    - DateTimeDigitized.\n"              \
        "t    - DateTime.\n"                       \
        "c    - File creation.\n"                  \
        "m    - File modification.\n"              \
        "rt   - Return.\n"                         \
        "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_rename_images_one_by_one(image_path: str, naming_style: str):
    returns_dict = {"rt": "return"}

    filename = os.path.basename(image_path)
    formatted_EXIF_DTO_date   = get_formatted_name(image_path, "EXIF_DTO", naming_style)
    formatted_EXIF_DTD_date   = get_formatted_name(image_path, "EXIF_DTD", naming_style)
    formatted_EXIF_DT_date    = get_formatted_name(image_path, "EXIF_DT", naming_style)
    formatted_FILE_CREAT_date = get_formatted_name(image_path, "FILE_CREAT", naming_style)
    formatted_FILE_MOD_date   = get_formatted_name(image_path, "FILE_MOD", naming_style)

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
            print("Enter - Skip.")

        print("rt    - Return.\n" \
              "exit  - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        if action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_rename_all_images(date_type: str):
    returns_dict = {"ls":  "list_images_new_names",
                    "rai": "rename_all_images",
                    "rt":  "return"}

    while True:
        print("Choose a renaming option:\n"                                     \
             f"ls   - List all images names converted to {date_type} format.\n" \
             f"rai  - Rename all images to {date_type} format.\n"               \
              "rt   - Return.\n"                                                \
              "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_rename_basis():
    returns_dict = {"o": "date_time_original",
                    "d": "date_time_digitized",
                    "t": "date_time",
                    "c": "file_creation",
                    "m": "file_modification",
                    "rt": "return"}

    while True:
        print("Choose style of renaming images:\n" \
        "o    - DateTimeOriginal.\n"               \
        "d    - DateTimeDigitized.\n"              \
        "t    - DateTime.\n"                       \
        "c    - File creation.\n"                  \
        "m    - File modification.\n"              \
        "rt   - Return.\n"                         \
        "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_rename_action():
    returns_dict = {"pfd": "print_dates_first_file",
                    "pad": "print_all_dates",
                    "roo": "rename_one_by_one",
                    "rai": "rename_all_images",
                    "cns": "change_naming_style",
                    "rt":  "return"}

    while True:
        print("Choose rename action: \n"                                \
        "pfd  - Print all dates of the first file in folder...\n"       \
        "pad  - Print all images names converted to a date format...\n" \
        "roo  - Rename images one by one...\n"                          \
        "rai  - Rename all images to a date format...\n"                \
        "cns  - Change naming style...\n"                               \
        "rt   - Return.\n"                                              \
        "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


def ask_naming_style(naming_style: str):
    returns_list = ["iso", "eu", "us", "rt"]

    while True:
        print(f"Current naming style: {naming_style}")
        print("Choose naming style:\n"               \
        "iso  - ISO 8601  IMG_[Y][M][D]_[H][M][S]\n" \
        "eu   - European  IMG_[D][M][Y]_[H][M][S]\n" \
        "us   - US Format IMG_[M][D][Y]_[H][M][S]\n" \
        "rt   - Return.\n"                           \
        "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        elif action not in returns_list:
            print("Incorrect input.\n")
        else:
            return action
