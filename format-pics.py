#!/usr/bin/env python
#
"""
This script will convert a folder of images and youtube videos
into an html or markdown file.
"""

import argparse
import os
import markdown


def write_image(file, img):
    file.write('![alt text](' + img + ')\n')


def write_youtube(file, link):
    file.write('[' + link + '](' + link + ')\n')


def write_subdir(file, dir):
    file.write('## ' + dir + '\n')


def write_header(file, dir):
    file.write('# ' + dir + '\n')


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.description = ('This script will convert a folder of images and'
                          ' youtube videos into an html and markdown.'
                          ' All youtube videos should be in files called youtube.txt.'
                          ' Each youtube.txt file must have one link per line.')
    parser.add_argument('-d', '--directory', type=str, default='./',
                        help='The directory to convet default current directory')
    parser.add_argument('-p', '--prefix', type=str, default='',
                        help='This string will be placed on the front of all image file paths')
    parser.add_argument('-o', '--output_file_name', type=str, default='formated_pics',
                        help='Name of the output file do not include the suffix i.e. .html or .md')

    # Get cmd line args
    args = parser.parse_args()

    # Check directory
    if not os.path.exists(args.directory):
        print 'The directory ' + args.directory + ' does not exist'
        exit(1)

    # Start output file
    with open(args.output_file_name + '.md', 'w') as out:
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

    # Convert the markdown to html
    with open(args.output_file_name + '.html', 'w') as out:
        markdown.markdownFromFile(input=args.output_file_name + '.md', output=out)


if __name__ == '__main__':
    main()
