from os import listdir, getcwd



def list_images_in_dir(format = "all"):
    """Lists all images in current directory with specified format."""
    valid_extensions = ()
    if format == "all":
        valid_extensions = ('jpg', 'jpeg', 'png', 'tiff', 'heic')
    elif format == "heic":
        valid_extensions = ('heic')
    elif format == "png":
        valid_extensions = ('png')
    else:
        raise Exception("module_main.py/list_images_in_dir error: Wrong format chosen.")

    for filename in listdir(getcwd()):
        if filename.lower().endswith(valid_extensions):
            print(filename)
