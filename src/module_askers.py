from os.path import exists



def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path


# ========================== MAIN ==========================
def ask_mainloop_action():
    while True:
        action = str(input("Enter action: \n" \
        "ls   - List all images in folder.\n" \
        "cd   - Change program working directory.\n" \
        "rnm  - Rename...\n" \
        "cnv  - Convert...\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["ls", "cd", "rnm", "cnv", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


# ========================= CONVERT =========================
def ask_convert_action():
    while True:
        action = str(input("Enter convert action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "lsp  - List all .png files in folder\n" \
        "htp  - .heic to .png...\n" \
        "ptj  - .png to .jpg...\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["lsh", "htp", "lsp", "ptj", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_htp_action():
    while True:
        action = str(input("Enter heic to png action: \n" \
        "lsh  - List all .heic files in folder\n" \
        "hpn  - Convert .heic files to .png files (leave heic files)\n" \
        "hpd  - Convert .heic files to .png files (delete heic files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["lsh", "hpn", "hpd", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


def ask_ptj_action():
    while True:
        action = str(input("Enter png to jpg action: \n" \
        "lsp  - List all .png files in folder\n" \
        "pjn  - Convert .png files to .jpg files (leave png files)\n" \
        "pjd  - Convert .png files to .jpg files (delete png files)\n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["lsp", "pjn", "pjd", "rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action


# ========================= RENAME =========================
def ask_rename_action():
    while True:
        action = str(input("Enter rename action: \n" \
        "rt   - Return.\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["rt", "exit"]:
            print("Incorrect input.\n")
        else:
            return action
