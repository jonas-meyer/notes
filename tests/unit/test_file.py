from unittest.mock import patch, mock_open
import pytest

from notes.file import File

filename = "test.txt"
text = "text"
directory = "test"


@pytest.fixture
def test_file():
    return File(filename, text)


@pytest.fixture()
def test_directory_file():
    return File(f"{directory}/{filename}", text)


def test_create_file(test_file):
    open_mock = mock_open()
    with patch("builtins.open", open_mock, create=True):
        test_file.create_file(test_file.filename)

    open_mock.assert_called_once_with(test_file.filename, "w", encoding="utf_8")


def test_append(test_file):
    open_mock = mock_open()
    with patch("builtins.open", open_mock, create=True):
        test_file.append()

    open_mock.assert_called_once_with(test_file.filename, "a", encoding="utf_8")
    open_mock.return_value.write.assert_called_once_with(f"\n{test_file.text}")


def test_replace(test_file):
    open_mock = mock_open()
    with patch("builtins.open", open_mock, create=True):
        test_file.replace()

    open_mock.assert_called_once_with(test_file.filename, "w", encoding="utf_8")
    open_mock.return_value.write.assert_called_once_with(test_file.text)


def test_open(test_directory_file):
    with patch("builtins.open", create=True) as open_mock, patch(
        "os.path.isdir"
    ) as isdir_mock, patch("os.makedirs", create=True) as mkdir_mock, patch(
        "os.path.exists"
    ) as exists_mock:
        isdir_mock.return_value = False
        exists_mock.return_value = False
        test_directory_file.open()

    exists_mock.assert_called_once_with(test_directory_file.filename)
    isdir_mock.assert_called_once_with(directory)
    open_mock.assert_called_once_with(
        test_directory_file.filename, "w", encoding="utf_8"
    )
    mkdir_mock.assert_called_once_with(directory)
