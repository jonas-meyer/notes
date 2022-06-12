import os
from datetime import datetime

import pytest
import shlex

from notes.args import parse_args


def cli_as_dict(str):
    cli = shlex.split(str)
    args = parse_args(cli)
    return vars(args)


def expected_args(**kwargs):
    now = datetime.now()
    default_args = {
        "filename": f"{os.getcwd()}/{now.strftime('%Y-%m-%d-%H-%M-%S')}.txt",
        "replace": False,
        "text": [],
    }
    return {**default_args, **kwargs}


def test_empty():
    assert cli_as_dict("") == expected_args()


def test_text_alone():
    assert cli_as_dict("lorem ipsum dolor sit amet") == expected_args(
        text=["lorem", "ipsum", "dolor", "sit", "amet"]
    )


def test_replace_alone():
    assert cli_as_dict("--replace") == expected_args(replace=True)
    assert cli_as_dict("-r") == expected_args(replace=True)


def test_filename_alone():
    assert cli_as_dict("--filename test.txt") == expected_args(filename="test.txt")
    assert cli_as_dict("-f test.txt") == expected_args(filename="test.txt")


@pytest.mark.parametrize(
    "cli",
    [
        "--replace --filename test.txt test_text",
        "--filename test.txt --replace test_text",
        "test_text --filename test.txt --replace",
    ],
)
def test_multiple(cli):
    result = expected_args(text=["test_text"], replace=True, filename="test.txt")
    assert cli_as_dict(cli) == result
