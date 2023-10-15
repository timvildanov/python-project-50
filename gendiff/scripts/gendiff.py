#!/usr/bin/env python3
from gendiff.cli import args_generate
from gendiff.tree_engine import generate_diff


def main():
    args = args_generate()
    print(generate_diff(*args))


if __name__ == '__main__':
    main()
