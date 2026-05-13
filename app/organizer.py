import logging
from app.utils import (
    convert_to_path,
    path_exists,
    path_is_folder,
    get_extension_folder_name,
    move_file,
    )

def organize_folder(path_string: str) -> None:
    if not path_string.strip():
        print("Error: folder path cannot be empty.")
        logging.error("Folder path cannot be empty.")
        return
    
    folder = convert_to_path(path_string)

    if not path_exists(folder):
        print("Error: the informed path does not exist.")
        logging.error(f"Path does not exist: {folder}")
        return

    if not path_is_folder(folder):
        print("Error: the informed path is not a folder.")
        logging.error(f"Path is not a folder: {folder}")
        return

    print(f"\nReading folder: {folder.resolve()}\n")
    logging.info(f"Reading folder: {folder.resolve()}")

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("The selected folder is empty or contains no files to organize.")
        logging.info(f"No files found in folder: {folder.resolve()}")
        return

    for item in files:
        extension = get_extension_folder_name(item)

        destination_folder = folder / extension
        destination_folder.mkdir(exist_ok = True)

        move_file(item, destination_folder)
