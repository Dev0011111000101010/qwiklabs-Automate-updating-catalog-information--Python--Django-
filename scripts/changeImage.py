#!/usr/bin/env python3

import os, sys
from PIL import Image
def image_3000x2000to600x400resizer_TIFF2JPEG_RGBA2RGB_converter():
    """This function changes the original photos located in ~/supplier-data/images
    Size: Change image resolution from 3000x2000 to 600x400 pixel
    Format: Change image format from .TIFF to .JPEG
    RGBA 4-channel format to RGB 3-channel format before processing the images
    """

    ## The path is received manually, for the script to work, you need to run the following commands
    ## In console
    ## python3
    ## import os
    ## os.getcwd() #in this case, the path "/home/student-00-8ffbbf494319/supplier-data/images"
    foto_originals_folder_absolute_path = '/home/student-00-8ffbbf494319/supplier-data/images'

    # According to the task given to us, the modified photos should appear in the same folder
    # Separate variable so that the result folder can be easily changed
    folder_converted_images = foto_originals_folder_absolute_path

    # Which files in the folder do not need to be edited as a photo
    # Currently only works if it's a single file or folder (locally work)
    ignore_file_list = ['.DS_Store', 'README']

    """Main control of the parameters of the results of modified files"""
    # File parameters after conversion
    resized_image_size = (600, 400)
    command_2_resize_photos = '.resize(resized_image_size)'
    command_2_convert_from_RGBA_2_RGB_convertion = ".convert('RGB')"
    command_folder_2_save_converted_photos_and_file_format = ".save(folder_converted_images, 'JPEG')"

    print('=============================')
    print('-----------------------------')
    print('# QA: checking if the folder where the photos are located is correctly defined')
    print('# QA: def image_3000x2000to600x400resizer_TIFF2JPEG_RGBA2RGB_converter():')
    print('-----------------------------')
    print(foto_originals_folder_absolute_path)
    print('-----------------------------')
    print('')

    for root, dirs, files in os.walk(foto_originals_folder_absolute_path):
        print('=============================')
        print('-----------------------------')
        print('# QA : initial list of files and their extensions')
        print('-----------------------------')
        for infile in files:
            # In MacOS, service files are generated that interfere with the script,
            # the library cannot understand what kind of file, service hidden folder,
            # for this reason, we added it to the exception
            if infile != ignore_file_list:
                image_path_and_name = os.path.join(root, infile)
                print('=============================')
                print('-----------------------------')
                print('# QA : print(infile)')
                print(infile)
                print('-----------------------------')
                print('# QA : print(root)')
                print(root)
                print('-----------------------------')
                print('# QA : print(image_path_and_name)')
                print(image_path_and_name)
                print('-----------------------------')
                print('')

            else:
                print('The folder contains files and folders that cannot be processed')
                print('Such folders need to be added to "ignore_file_list"')
                pass






launch_photo_change_function = image_3000x2000to600x400resizer_TIFF2JPEG_RGBA2RGB_converter()