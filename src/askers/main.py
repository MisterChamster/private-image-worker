import os
from tkinter import filedialog



def ask_mainloop_action():
    while True:
        print("Choose action: \n" \
        "ls   - List all images in folder.\n" \
        "cd   - Change program working directory.\n" \
        "rnm  - Rename...\n" \
        "cnv  - Convert...\n" \
        "exit - Exit program.\n\n>> ", end="")
        action = str(input())

        if action == "exit":
            return None
        if action not in ["ls", "cd", "rnm", "cnv"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_path_filedialog(type: str, message: str):
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    sel_path = ""
    if type == "f":
        sel_path = filedialog.askopenfilename(title=message)
    elif type == "d":
        sel_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    return sel_path


# def ask_path():
#     while True:
#         print("Enter path\n(to exit input 'exit'): \n>> ", end="")
#         dir_path = str(input())
#         if os.path.exists(dir_path) or dir_path == "exit":
#             return dir_path
#         else:
#             print("Invalid path.\n")
