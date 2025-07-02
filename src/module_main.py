from .module_askers import ask_path, ask_mainloop_action, ask_convert_action
from os import chdir, listdir, getcwd



def list_images_in_dir(format = "all"):
    """Lists all images in current directory."""
    valid_extensions = ()
    if format == "all":
        valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')
    elif format == "heic":
        valid_extensions = ('.heic')
    elif format == "png":
        valid_extensions = ('.png')
    else:
        raise Exception("module_main.py/list_images_in_dir error: Wrong format chosen.")

    for filename in listdir(getcwd()):
        if filename.lower().endswith(valid_extensions):
            print(filename)


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
            print()
            ask_convert_action()
        elif action == "exit":
            break
