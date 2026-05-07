from pathlib import Path

def convert_to_path(path_string: str) -> Path:
    return Path(path_string)

def path_exists(path: Path) -> bool:
    return path.exists()

def path_is_folder(path: Path) -> bool:
    return path.is_dir()
