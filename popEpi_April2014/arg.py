# arg.py

import argparse
import sys

def int_args(args=None):
    parser = argparse.ArgumentParser(description='Processing integers.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='integer args')
    return parser.parse_args()

if __name__ == '__main__':
    print int_args(sys.argv[1:])