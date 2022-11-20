#!/usr/bin/env python3

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

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
    foto_originals_folder_absolute_path = '/home/student-00-0dd6461e8915/supplier-data/images/'

    # According to the task given to us, the modified photos should appear in the same folder
    # Separate variable so that the result folder can be easily changed
    folder_converted_images_absolute_path = foto_originals_folder_absolute_path

    # Which files in the folder do not need to be edited as a photo
    # Currently only works if it's a single file or folder (locally work)
    ignore_file_list = ['.DS_Store', 'README', 'LICENSE']

    """Main control of the parameters of the results of modified files"""
    # File parameters after conversion
    # Intermediate variable
    resized_image_size = 600, 400
    # Variables to use in "PIL"
    command_2_resize_photos = '.resize(resized_image_size)'
    command_2_convert_from_RGBA_2_RGB_convertion = ".convert('RGB')"
    command_folder_2_save_converted_photos_and_file_format = ".save(folder_converted_images_absolute_path + infile[:-4] +'jpeg', 'JPEG')"

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
        print('')
        for infile in files:
            # In MacOS, service files are generated that interfere with the script,
            # the library cannot understand what kind of file, service hidden folder,
            # for this reason, we added it to the exception
            if infile not in ignore_file_list:
                # The universal "correct" way to connect the filename of each photo
                # with an absolute path of their original location
                image_path_and_name = os.path.join(root, infile)
                # print('=============================')
                # print('-----------------------------')
                # print('# QA : print(infile)')
                # print(infile)
                # print('-----------------------------')
                # print('# QA : print(root)')
                # print(root)
                # print('-----------------------------')
                # print('# QA : print(image_path_and_name)')
                # print(image_path_and_name)
                # print('-----------------------------')
                # print('')

                # The universal "correct" way to connect the filename of each photo
                # with an absolute path of their new location
                new_image_path_and_name = os.path.join(folder_converted_images_absolute_path, infile)

                # "PIL" command of open image
                im = Image.open(image_path_and_name)

                # print('=============================')
                # print('-----------------------------')
                # print('# QA : old image path and name')
                # print(image_path_and_name)
                # print('-----------------------------')
                # # print(im)
                # print(im.format, im.size, im.mode)
                # if ERROR "tempfile.tif: JPEG compression support is not configured."
                # go to https://gitlab.gnome.org/GNOME/gimp/-/issues/5651
                # print('-----------------------------')
                # print('')

                im_convert_working_summary_of_commands = 'im' + command_2_resize_photos + command_2_convert_from_RGBA_2_RGB_convertion + command_folder_2_save_converted_photos_and_file_format
                # print('=============================')
                # print('-----------------------------')
                # print('# QA: im_convert_working_summary_of_commands')
                # print(im_convert_working_summary_of_commands)
                # print('-----------------------------')
                # print('')
                # print('=============================')
                # print('-----------------------------')
                # print(im)
                # print('-----------------------------')
                # print('')

                try:
                    convert = im.resize(resized_image_size).convert('RGB').save(folder_converted_images_absolute_path + infile[:-4] +'jpeg', 'JPEG')
                    # convert = im_convert_working_summary_of_commands
                    print('-----------------------------')
                    print('print(convert)')
                    print(convert)
                    print('-----------------------------')

                    # print(im.format, im.size, im.mode)
                    # im.save(folder_converted_images_absolute_path + infile[:-4] +'jpeg', 'JPEG')
                    # print(im.format, im.size, im.mode)

                    print('# Success: photo modified successfully')
                    print(image_path_and_name)
                    print(im.format, im.size, im.mode)
                    # im_convert_working_summary_of_commands
                    new_im = Image.open(new_image_path_and_name[:-4] +'jpeg')
                    print('# QA : converted photo properties')
                    print(new_image_path_and_name[:-4] +'jpeg')
                    print(new_im.format, new_im.size, new_im.mode)
                    print('-----------------------------')

                except OSError as error:
                    print('=============================')
                    print('-----------------------------')
                    print(error)
                    print("Cannot convert: ", image_path_and_name)
                    print(im.format, im.size, im.mode)
                    print('-----------------------------')
                    print('')


                print('-----------------------------')
                print(os.path.join(root, infile))
                print(image_path_and_name + '   # Should equal the string above, checking for identity with "os.path.join(root, infile)"')
                print('-----------------------------')
                print('')

            else:
                print('=============================')
                print('-----------------------------')
                print('The folder contains files and folders that cannot be processed')
                print('# "' + infile + '"' + " = an example of such a file")
                print('Such folders need to be added to "ignore_file_list"')
                print('-----------------------------')
                print('')
                pass






launch_photo_change_function = image_3000x2000to600x400resizer_TIFF2JPEG_RGBA2RGB_converter()