import os
import sys
import argparse

from validate_directory import ValidateDirectory


def main():
    parser = _create_arg_parser()
    args = parser.parse_args()

    output = args.output
    if output:
        output = open(output, "w")
    else:
        output = sys.stdout

    for filename in os.listdir(args.source):
        with open(f"{args.source}/{filename}") as file:
            line = file.readline()
            while line:
                _print_line(line, output)
                line = file.readline()


def _print_line(line, output):
    if len(line.strip()) < 1:
        return
    if "<doc" in line or "</doc" in line:
        return

    print(line, file=output, end="")


def _create_arg_parser():
    parser = argparse.ArgumentParser(description="merge files into a single document")
    parser.add_argument("--source", required=True, help="source directory, which contains the files to be merged", action=ValidateDirectory)
    parser.add_argument("--output", required=False, help="output file to write to")
    return parser


if __name__ == "__main__":
    main()
