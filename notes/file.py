import os.path
import sys


class File:
    """Creates a file with the given filename and text"""

    def __init__(self, filename, text):
        self.filename = filename
        self.text = text

    def open(self):
        filename = self.filename
        directory = os.path.dirname(filename)
        if not directory:
            directory = os.getcwd()
        if not os.path.exists(filename):
            if not os.path.isdir(directory):
                os.makedirs(directory)
                print(f"Directory {directory} created", file=sys.stderr)
            self.create_file(filename)
            print(f"File created at {filename}", file=sys.stderr)
        return self

    @staticmethod
    def create_file(filename):
        with open(filename, "w", encoding="utf_8"):
            pass

    def replace(self):
        with open(self.filename, "w", encoding="utf_8") as f:
            f.write(self.text)

    def append(self):
        with open(self.filename, "a", encoding="utf_8") as f:
            f.write(f"\n{self.text}")


def open_file(filename, text):
    return File(filename, text).open()
