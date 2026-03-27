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

    dir_list = get_files_list(dir_path)
    for file_path in dir_list:
        if file_path.suffix.lower() in valid_extensions:
            print(file_path.name)


def get_files_list(dir_path: Path, ext: str = "any") -> list[Path]:
    if not dir_path.is_dir():
        raise Exception("That is not a directory!!\n")

    nodes_list = []
    for node in dir_path.iterdir():
        if (node.is_file() and
            not node.stem.startswith(".")):
            nodes_list.append(node)

    if ext != "any":
        nodes_list = [
            a for a in nodes_list
            if (a.suffix == ext)]

    nodes_list.sort()
    return nodes_list


def get_nodes_list(dir_path: Path) -> list[Path]:
    if not dir_path.is_dir():
        raise Exception("That is not a directory!!\n")

    nodes_list = []
    for node in dir_path.iterdir():
        if not node.name.startswith("."):
            nodes_list.append(node)

    nodes_list.sort()
    return nodes_list
