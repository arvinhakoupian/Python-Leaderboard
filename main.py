import sys

from handler import Handler


def main(argv):
    Handler(print).run(argv)


if __name__ == "__main__":
    main(sys.argv)
