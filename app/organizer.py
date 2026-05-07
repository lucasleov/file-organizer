from app.utils import (
    convert_to_path,
    path_exists,
    path_is_folder,
    get_extension_folder_name,
    )

def organize_folder(path_string: str) -> None:
    folder = convert_to_path(path_string)

    if not path_exists(folder):
        print("Error: the informed path does not exist.")
        return

    if not path_is_folder(folder):
        print("Error: the informed path is not a folder.")
        return

    print(f"\nReading folder: {folder.resolve()}\n")

    for item in folder.iterdir():
        if item.is_file():
            extension = get_extension_folder_name(item)

            destination_folder = folder / extension
            destination_folder.mkdir(exist_ok = True)

            destination_path = destination_folder / item.name

            item.rename(destination_path)

            print(f"Moved: {item.name} -> {destination_folder.name}/")
