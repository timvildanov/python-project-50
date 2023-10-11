import argparse

def args_generate():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='%(prog)s [options] <filepath1> <filepath2>',
        description='Generate difference 2 files')

    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        default='string', type=str,
        help='set format of output',)

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format