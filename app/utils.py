from pathlib import Path

def convert_to_path(path) -> Path:
    return Path(path)

def path_exists(path) -> bool:
    return path.exists()

def path_is_folder(path) -> bool:
    return path.is_dir()
