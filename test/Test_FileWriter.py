import pytest

from src.FileWriter import FileWriter


@pytest.fixture
def file_writer():
    return FileWriter()

def test_write_data_to_file(file_writer, tmp_path):
    file_path = tmp_path / "test_file.txt"

    file_writer.write(file_path, "Test data")

    with open(file_path, 'r') as file:
        content = file.read()

    assert content == "Test data"

def test_write_to_nonexistent_directory(file_writer):
    with pytest.raises(Exception) as excinfo:
        file_writer.write("nonexistent_directory/test_file.txt", "Test data")

    assert str(excinfo.value) == "Can't open file[Errno 2] No such file or directory: 'nonexistent_directory/test_file.txt'"