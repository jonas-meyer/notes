# Notes
Notes is a cli tool that allows the user to create notes quickly using the commandline.

## Installation
1. Install Poetry to your system ([poetry docs](https://python-poetry.org/docs/))
2. Run the command `make install`
3. Run the command `poetry shell` in order to enable the virtual environment and run the cli tool

Further make commands can be viewed in the MAKEFILE

## Usage
```commandline
# Creates a file in the current working directory with the filename 
# YYYY-MM-DD-HH-MM-SS.txt with the content Hello World!
notes Hello World!

# Replaces the content in file test.txt if it exists with Hello World!
notes Hello World! --replace --filename test.txt

# Creates or appends (in a newline) to a file in a directory with Hello World!
notes Hello World! --filename directory/test.txt
```
Commandline arguments can be given in any order

`--replace or -r` can be used

`--filename or -f` can be used

## Testing
unit tests are found in "tests/unit" and can be run with `make unit`
