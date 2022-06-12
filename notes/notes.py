from .file import open_file


def run(args):
    write(args)


def write(args):
    text = " ".join(args.text).strip()
    if not text or text.isspace():
        raise Exception("Did not receive any text!")

    file = open_file(args.filename, text)
    if args.replace:
        file.replace()
    else:
        file.append()

    print(f"Wrote note to {args.filename}")
