#!/usr/bin/env python
#
"""
This script will convert a folder of images and youtube videos
into an html or markdown file.
"""

import argparse
import os


def write_image_md(file, img):
    file.write('[[' + img + ']]\n')


def write_image_html(file, img):
    pass


def write_youtube_md(file, link):
    file.write('[' + link + '](' + link + ')\n')


def write_youtube_html(file, link):
    pass


def write_subdir_md(file, dir):
    file.write('## ' + dir + '\n')


def write_subdir_html(file, dir):
    pass


def write_header_md(file, dir):
    file.write('# ' + dir + '\n')


def write_header_html(file, dir):
    pass


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
    parser.add_argument('-p', '--prefix', type=str, default='',
                        help='This string will be placed on the front of all image file paths')

    # Get cmd line args
    args = parser.parse_args()

    # Output file
    output_file_name = 'formated_pics'
    # Writing functions
    write_image = None
    write_youtube = None
    write_subdir = None
    write_header = None

    # Check format
    if args.format == 'markdown':
        # print 'Sorry markdown hasn\'t been implemented yet'
        # exit()
        output_file_name += '.md'
        write_image = write_image_md
        write_youtube = write_youtube_md
        write_subdir = write_subdir_md
        write_header = write_header_md
    elif args.format == 'html':
        print 'Sorry html hasn\'t been implemented yet'
        exit()
        output_file_name += '.html'
        write_image = write_image_html
        write_youtube = write_youtube_html
        write_subdir = write_subdir_html
        write_header = write_header_html

    # Check directory
    if not os.path.exists(args.directory):
        print 'The directory ' + args.directory + ' does not exist'
        exit()

    # Start output file
    with open(output_file_name, 'w') as out:
        # Initial writes
        write_header(out, args.directory)

        # Itterate over all files in args.directory
        for root, dirs, filenames in os.walk(args.directory):
            # Subdir heading
            write_subdir(out, root)

            # Write all images and videos
            for f in filenames:
                if f != 'youtube.txt':
                    write_image(out, args.prefix + os.path.join(root, f))
                else:
                    with open(os.path.join(root, f), 'r') as youtube:
                        for link in youtube:
                            write_youtube(out, link[0:-1])


if __name__ == '__main__':
    main()
