#!/usr/bin/env python
#
"""
This script will convert a folder of images and youtube videos
into an html or markdown file.
"""

import argparse
import os


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.description = ('This script will convert a folder of images and'
                          ' youtube videos into an html or markdown file.')
    parser.add_argument('-f', '--format', choices=['markdown', 'html'], type=str,
                        default='markdown',
                        help='Choose the format of the output file default markdown')
    parser.add_argument('-d', '--directory', type=str, default='./',
                        help='The directory to convet default current directory')

    # Get cmd line args
    args = parser.parse_args()

    # Output file
    output_file_name = 'formated_pics'

    # Check format
    if args.format == 'markdown':
        print 'Sorry markdown hasn\'t been implemented yet'
        exit()
        output_file_name += '.md'
    elif args.format == 'html':
        print 'Sorry html hasn\'t been implemented yet'
        exit()
        output_file_name += '.html'

    # Check directory
    if not os.path.exists(args.directory):
        print 'The directory ' + args.directory + ' does not exist'
        exit()

    # Start output file
    with open(output_file_name, 'w') as out:
        # Itterate over all files in args.directory
        for root, dirs, filenames in os.walk(args.directory):
            out.write(str([root, dirs, filenames]) + '\n')


if __name__ == '__main__':
    main()
