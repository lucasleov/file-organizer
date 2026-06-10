from pathlib import Path
from app.utils import (
    get_extension_folder_name,
    path_exists,
    path_is_folder,
    convert_to_path,
    move_file,
    )

def test_get_extension_folder_name_normal_extension():
    file_path = Path("photo.jpg")

    result = get_extension_folder_name(file_path)

    assert result == "jpg"

def test_get_extension_folder_name_uppercase_extension():
    file_path = Path("document.PDF")

    result = get_extension_folder_name(file_path)

    assert result == "pdf"

def test_get_extension_folder_name_without_extension():
    file_path = Path("README")

    result = get_extension_folder_name(file_path)

    assert result == "no_extension"

def test_get_extension_folder_name_multiple_dots():
    file_path = Path("backup.final.zip")

    result = get_extension_folder_name(file_path)

    assert result == "zip"

def test_get_extension_folder_name_hidden_file_without_extension():
    file_path = Path(".gitignore")

    result = get_extension_folder_name(file_path)

    assert result == "no_extension"

def test_path_exists_existing_path(tmp_path):
    result = path_exists(tmp_path)

    assert result is True

def test_path_exists_non_existing_path(tmp_path):
    fake_path = tmp_path / "missing_folder"

    result = path_exists(fake_path)

    assert result is False

def test_path_is_folder_with_folder(tmp_path):
    result = path_is_folder(tmp_path)

    assert result is True

def test_path_is_folder_with_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("content")

    result = path_is_folder(file_path)

    assert result is False

def test_convert_to_path_returns_path_object():
    result = convert_to_path("my_folder")

    assert result == Path("my_folder")

def test_move_file_moves_file_to_destination(tmp_path):
    source_file = tmp_path / "photo.jpg"
    destination_folder = tmp_path / "jpg"

    source_file.write_text("fake image content")
    destination_folder.mkdir()

    move_file(source_file, destination_folder)

    destination_file = destination_folder / "photo.jpg"

    assert destination_file.exists()
    assert not source_file.exists()
