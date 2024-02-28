import argparse
from app.engine import get_tiff_file


def get_args():
    parser = argparse.ArgumentParser(
        description="Add the path to the folder"
    )
    parser.add_argument('direct')
    return parser.parse_args()


def main():
    args = get_args()
    return get_tiff_file(args.direct)


if __name__ == '__main__':
    main()
