import os



# ========================== MAIN ==========================
def ask_mainloop_action():
    while True:
        print("Choose action: \n" \
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
        print("Enter path\n(to exit input 'exit'): \n>> ", end="")
        dir_path = str(input())
        if os.path.exists(dir_path) or dir_path == "exit":
            return dir_path
        else:
            print("Invalid path.\n")
