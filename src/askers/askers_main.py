import os
from pathlib import Path
from typing import Literal
from tkinter import filedialog



def ask_mainloop_action() -> str | None:
    returns_dict = {
        "ls":  "list",
        "cd":  "change_dir",
        "rnm": "rename",
        "cnv": "convert",
        "e":   "exit"}

    while True:
        print("Choose action: \n"
              "ls  - List all images in folder\n"
              "cd  - Change program working directory\n"
              "rnm - Rename...\n"
              "cnv - Convert...\n"
              "e   - Exit program\n>> ", end="")
        action = input().strip().lower()

        if action in returns_dict:
            return returns_dict[action]
        print("Incorrect input.\n")


def ask_path_filedialog(
        node_type: Literal["file", "dir"],
        message: str
        ) -> Path | None:
    original_path = Path.cwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    sel_path = ""
    if node_type == "file":
        sel_path = filedialog.askopenfilename(title=message)
    elif node_type == "dir":
        sel_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    if sel_path == "":
        return

    return Path(sel_path)
