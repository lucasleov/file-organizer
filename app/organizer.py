from app.utils import convert_to_path, path_exists, path_is_folder

def organize_folder(path_string) -> None:
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
            print(f"File found: {item.name} | Extension: {item.suffix}")
