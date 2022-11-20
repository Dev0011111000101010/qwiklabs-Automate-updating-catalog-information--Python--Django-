#!/usr/bin/env python3

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

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
ignore_file_list = ['.DS_Store', 'README', 'LICENSE', '*.tiff']

print('=============================')
print('-----------------------------')
print('# QA: checking if the folder where the photos are located is correctly defined')
print('# supplier_image_upload.py')
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
        # The target folder contains folders and TIFF files that do not need to be uploaded to the server
        # For this reason, we only select JPEG files
        if infile[-4:] == 'jpeg':
            # The universal "correct" way to connect the filename of each photo
            # with an absolute path of their original location
            image_path_and_name = os.path.join(root, infile)
            print('=============================')
            print('-----------------------------')
            print('# QA : print(infile)')
            print(infile)
            print(infile[-4:] + "# infile[-4:]")
            print('-----------------------------')
            print('# QA : print(root)')
            print(root)
            print('-----------------------------')
            print('# QA : print(image_path_and_name)')
            print(image_path_and_name)
            print('-----------------------------')
            print('')

            # Uploading all JPEG files to the server
            with open(image_path_and_name, 'rb') as opened:
                r = requests.post(url, files={'file': opened})

