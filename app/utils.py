import logging
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
        logging.info(f"Moved: {file} -> {destination_path}")
    except FileExistsError:
        print(f"Error: a file named {file.name} already exists in {destination_folder.name}/.")
        logging.error(f"File already exists: {destination_path}")
    except PermissionError:
        print(f"Error: permission denied while moving {file.name}.")
        logging.error(f"Permission denied while moving {file}")
    except OSError as error:
        print(f"Error while moving {file.name}: {error}")
        logging.error(f"Error while moving {file}: {error}")

def setup_logging() -> None:
    logs_folder = Path("logs")
    logs_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=logs_folder / "file_organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        )
