from pathlib import Path
from typing import Literal



def list_images_in_dir(
        dir_path: Path,
        format: Literal["all", "heic", "png", "jpg"] = "all"
        ) -> None:
    """Lists all images in current directory with specified format."""
    valid_extensions = ()
    if format == "all":
        valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.heic')
    elif format == "heic":
        valid_extensions = ('.heic')
    elif format == "png":
        valid_extensions = ('.png')
    elif format == "jpg":
        valid_extensions = ('.jpg', '.jpeg')
    else:
        raise Exception("module_main.py/list_images_in_dir error: Wrong format chosen.")

    for file_path in dir_path.iterdir():
        if (file_path.suffix.lower() in valid_extensions and
            not file_path.stem.startswith(".")):
            print(file_path)
