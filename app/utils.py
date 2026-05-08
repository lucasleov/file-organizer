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
