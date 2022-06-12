import argparse
import os
from datetime import datetime


def parse_args(args=None):
    now = datetime.now()
    if args is None:
        args = []
    parser = argparse.ArgumentParser(
        add_help=True, description="Create notes using the cmdline"
    )

    parser.add_argument_group("Singular Commands")

    description_text = """
    To create a new note, just write it on the command line! E.g:
    notes Hello World!
    Without any further commands the text file is saved in the current 
    directory """

    writing = parser.add_argument_group("Writing", description_text)
    writing.add_argument("text", metavar="", nargs="*")

    config = parser.add_argument_group("Configuration commands")
    config.add_argument(
        "--filename",
        dest="filename",
        type=str,
        default=f"{os.getcwd()}/{now.strftime('%Y-%m-%d-%H-%M-%S')}.txt",
        help="""Overrides the default filename and directory ( 
        current_directory/YYYY-MM-DD-HH-MM-SS.txt). If no directory is given 
        then the file is written in the current working directory """,
    )
    config.add_argument(
        "-f", dest="filename", type=str, default="", help=argparse.SUPPRESS
    )
    config.add_argument(
        "--replace",
        action=argparse.BooleanOptionalAction,
        dest="replace",
        type=bool,
        default=False,
        help="""
        Replaces the content of an existing file. Optional command, if not 
        given then text will be appended to existing file.
        """,
    )
    config.add_argument(
        "-r",
        action=argparse.BooleanOptionalAction,
        dest="replace",
        type=bool,
        default=False,
        help=argparse.SUPPRESS,
    )

    return parser.parse_intermixed_args(args)
