from os.path import exists
from os import listdir



def ask_path():
    while True:
        dir_path = str(input("Enter path: \n>> "))
        if exists(dir_path):
            return dir_path


def list_images_in_dir(directory):
    """Lists all images in current directory."""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')

    for filename in listdir(directory):
        if filename.lower().endswith(valid_extensions):
            print(filename)


def ask_mainloop_action():
    while True:
        action = str(input("Enter action: \nls - List all images in folder.\nexit - Exit program.\n\n>> "))

        if action not in ["ls", "exit"]:
            print("Incorrect input!!")

        else:
            return action


def mainloop():
    while True:
        action = ask_mainloop_action()
        if action == "ls":
            pass
        elif action == "exit":
            break
