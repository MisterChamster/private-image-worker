from os.path import exists
from os import chdir, listdir, getcwd



def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path


def list_images_in_dir():
    """Lists all images in current directory."""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')

    for filename in listdir(getcwd()):
        if filename.lower().endswith(valid_extensions):
            print(filename)


def ask_mainloop_action():
    while True:
        action = str(input("Enter action: \n" \
        "ls - List all images in folder.\n" \
        "cnv - Convert...\n" \
        "exit - Exit program.\n\n>> "))

        if action not in ["ls", "cnv", "exit"]:
            print("Incorrect input!!")

        else:
            return action


def ask_convert_action():
    pass


def mainloop():
    print()
    dir_main = ask_path()
    chdir(dir_main)

    while True:
        print()
        action = ask_mainloop_action()
        if action == "ls":
            list_images_in_dir()
            print()
        elif action =="cnv":
            ask_convert_action()
        elif action == "exit":
            break
