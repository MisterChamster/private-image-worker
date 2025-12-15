import os
from tkinter import filedialog



def ask_mainloop_action():
    returns_dict = {"ls": "list",
                    "cd": "change_dir",
                    "rnm": "rename",
                    "cnv": "convert"}

    while True:
        print("Choose action: \n"
        "ls   - List all images in folder.\n"
        "cd   - Change program working directory.\n"
        "rnm  - Rename...\n"
        "cnv  - Convert...\n"
        "exit - Exit program.\n\n>> ", end="")
        action = input().strip()

        if action == "exit":
            return None
        if action in returns_dict:
            return returns_dict[action]
        else:
            print("Incorrect input.\n")


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
