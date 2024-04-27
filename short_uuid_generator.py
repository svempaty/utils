#!/usr/bin/python3

import argparse
import base64
import uuid

MIN_UUIDS = 1
MAX_UUIDS = 1000

def generate_short_uuid():
    # Generate a random UUID
    random_uuid = uuid.uuid4().bytes

    # Encode the UUID using Base64
    encoded_uuid = base64.b64encode(random_uuid)

    # Take the first 8 characters of the encoded UUID
    short_uuid = encoded_uuid[:8].lower()

    return short_uuid.decode('utf-8')

def main():
    # Number of uuids to generate is an argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, 
                        help='Number of uuids to generate, between {min} and {max}. Defaults to {min}.'
                        .format(min=MIN_UUIDS, max=MAX_UUIDS))
    args = parser.parse_args()

    if args.number is not None and (args.number <= MIN_UUIDS or args.number >= MAX_UUIDS):
        parser.print_help()
        exit()

    num = args.number or MIN_UUIDS
    for _ in range(num):
        print(generate_short_uuid())

if __name__ == '__main__':
    main()
