#!/usr/bin/python3

import argparse
import random
import string

ID_LEN = 6
MIN_IDS = 1
MAX_IDS = 1000

def generate_random_id(len):
    # Generate alphanumeric string
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(len))
    return result_str

def main():
    # Number of ids to generate is an argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, 
                        help='Number of ids to generate, between {min} and {max}. Defaults to {min}.'
                        .format(min=MIN_IDS, max=MAX_IDS))
    args = parser.parse_args()

    if args.number is not None and (args.number <= MIN_IDS or args.number >= MAX_IDS):
        parser.print_help()
        exit()

    num = args.number or MIN_IDS

    for _ in range(num):
        print(generate_random_id(ID_LEN))

if __name__ == '__main__':
    main()
