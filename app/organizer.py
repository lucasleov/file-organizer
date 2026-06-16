import logging
from app.utils import (
    convert_to_path,
    path_exists,
    path_is_folder,
    get_extension_folder_name,
    move_file,
    )

def organize_folder(path_string: str) -> None:
    if not path_is_valid(path_string):
        return
    
    folder = convert_to_path(path_string)

    print(f"\nReading folder: {folder.resolve()}\n")
    logging.info(f"Reading folder: {folder.resolve()}")

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("The selected folder is empty or contains no files to organize.")
        logging.info(f"No files found in folder: {folder.resolve()}")
        return

    for item in files:
        
        destination_folder = get_destination_folder(item, folder)
        destination_folder.mkdir(exist_ok = True)
        
        move_file(item, destination_folder)

def path_is_valid(path_string):
    if not path_string.strip():
        print("\nError: folder path cannot be empty.")
        logging.error("Folder path cannot be empty.")
        return False
    
    folder = convert_to_path(path_string)

    if not path_exists(folder):
        print("\nError: the informed path does not exist.")
        logging.error(f"Path does not exist: {folder}")
        return False

    if not path_is_folder(folder):
        print("\nError: the informed path is not a folder.")
        logging.error(f"Path is not a folder: {folder}")
        return False

    return True

def get_destination_folder(item, folder):
    extension = get_extension_folder_name(item)
    return folder / extension
