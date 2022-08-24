import argparse, os
from pathlib import Path

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=dir_path)
    args = parser.parse_args()
    path = Path(args.path) if args.path else Path(os.getcwd())
    resolved_path = path.resolve()


if __name__ == "__main__":
    main()
