from pathlib import Path


def convert_to_path(path_string: str) -> Path:
    return Path(path_string)


def path_exists(path: Path) -> bool:
    return path.exists()


def path_is_folder(path: Path) -> bool:
    return path.is_dir()


def get_extension_folder_name(path: Path) -> str:
    extension = path.suffix.lower().replace(".", "")

    if extension == "":
        return "no_extension"

    return extension


def move_file(file: Path, destination_folder: Path) -> None:
    destination_path = destination_folder / file.name
    
    try:
        file.rename(destination_path)
        print(f"Moved: {file.name} -> {destination_folder.name}/")
    except FileExistsError:
        print(f"Error: a file named {file.name} already exists in {destination_folder.name}/.")
    except PermissionError:
        print(f"Error: permission denied while moving {file.name}.")
    except OSError as error:
        print(f"Error while moving {file.name}: {error}")
