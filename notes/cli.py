import sys

from .args import parse_args
from .notes import run


def cli():
    args = parse_args(sys.argv[1:])
    run(args)
