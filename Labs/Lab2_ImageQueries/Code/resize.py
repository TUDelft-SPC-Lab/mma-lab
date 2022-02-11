#!/usr/bin/env python

import argparse
import glob

from PIL import Image

parser = argparse.ArgumentParser(description="Resize tool to resize a batch of images.")
parser.add_argument("image_path", help="The path to the images")
parser.add_argument("width", help="New width in pixels")
parser.add_argument("--height",
                    help="New height in pixels, when preserve is enabled, this value is ignored",
                    default=100)
parser.add_argument("-p", "--preserve",
                    help="Preserve aspect ratio. set to 'False' to disable. Default is True",
                    default='true')
parser.add_argument("-o", "--output",
                    help="Output path for resize images. If not specified, original images will be overwritten",
                    default='')

args = parser.parse_args()

print("\nResize tool")
print("============\n")

# retrieve image list

types = ('*.jpg', '*.JPG', '*.png')
image_list = []
for type_ in types:
    print(type_, ' ', image_list)
    files = args.image_path + type_
    image_list.extend(glob.glob(files))

for image in image_list:
    im = Image.open(image)
    width, height = im.size
    new_width = int(args.width)
    if args.preserve.lower() == 'true':
        ratio = float(width) / new_width
        new_height = int(height / ratio)
    else:
        new_height = int(args.height)
    im = im.resize((new_width, new_height))
    if (args.output != ''):
        outfile = args.output + '/' + image.split('/')[-1]
    else:
        outfile = image

    print('resized: ', outfile)

    # Get the EXIF data and store it together with the image

    if 'exif' in im.info:
        exif = im.info['exif']
        im.save(outfile, exif=exif)
    else:
        im.save(outfile)
