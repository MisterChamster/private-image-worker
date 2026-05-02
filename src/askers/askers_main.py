from os import chdir, path
from pathlib import Path
from typing import Literal
from tkinter import filedialog



def ask_mainloop_action() -> Literal[
    "list",
    "change_dir",
    "rename",
    "convert",
    "exit"]:
    returns_dict = {
        "ls":  "list",
        "rn": "rename",
        "cv": "convert",
        "cd":  "change_dir",
        "x":   "exit"}

    while True:
        print("Choose action: \n"
              "ls - List all images in folder\n"
              "rn - Rename...\n"
              "cv - Convert...\n"
              "cd - Change program working directory\n"
              "x  - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_path_filedialog(
        node_type: Literal["file", "dir"],
        message: str
        ) -> Path | None:
    original_path = Path.cwd()
    desktop_path = path.join(path.expanduser("~"), "Desktop")
    chdir(desktop_path)

    sel_path = ""
    if node_type == "file":
        sel_path = filedialog.askopenfilename(title=message)
    elif node_type == "dir":
        sel_path = filedialog.askdirectory(title=message)

    chdir(original_path)
    if sel_path == "":
        return

    return Path(sel_path)
