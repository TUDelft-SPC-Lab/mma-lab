from typing import Any

import glob
import argparse
from PIL import Image


def resize(image_path, new_width, output_path):
    print ("Resize tool")
    print ("============")

    # retrieve image list

    types = ('*.jpg', '*.JPG', '*.png')
    image_list = []
    for type_ in types:
        print (type_, ' ', image_list)
        files = image_path + type_
        print(image_path+type_)
        image_list.extend(glob.glob(files))

    for image in image_list:
        print(image)
        im = Image.open(image)
        width, height = im.size
        ratio = float(width)/new_width
        new_height = int(height / ratio)
        im = im.resize((new_width, new_height))
        if output_path != '':
            outfile = output_path +'/'+ (image.split('/')[-1]).split("\\")[-1]
        else:
            outfile = image
    
        print ('resized: ', outfile)
    
        # Get the EXIF data and store it together with the image

        if 'exif' in im.info:
            exif = im.info['exif']
            im.save(outfile, exif=exif)
        else:
            im.save(outfile)
