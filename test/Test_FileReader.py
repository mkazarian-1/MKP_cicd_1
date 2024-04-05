import pytest

from src.FileReader import FileReader


@pytest.fixture
def file_reader():
    return FileReader()

def test_read_existing_file(file_reader):
    filename = 'test.txt'
    with open(filename, 'w') as file:
        file.write('This is a test file.')

    data = file_reader.read(filename)

    assert data == 'This is a test file.'

def test_read_nonexistent_file(file_reader):
    with pytest.raises(Exception) as excinfo:
        file_reader.read('nonexistent.txt')

    # Check if the exception message is correct
    assert str(excinfo.value) == "Can't open file[Errno 2] No such file or directory: 'nonexistent.txt'"