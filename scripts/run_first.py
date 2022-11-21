#!/usr/bin/env python3

## Run in comand line BEFORE run the script
# sudo apt-get update
# sudo apt install python-django-common
# sudo systemctl start google-startup-scripts.service
# nano ~/run_first.py
# sudo chmod +x ~/run_first.py
# ./run_first.py

"""First, before running
    run.py
    , you need to run the file
    run_first.py """

import os

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

## This folder stores TXT files for the site
## The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
"""Online"""
fruits_list_txt_files_folder_path = os.getcwd() + '/supplier-data/descriptions/'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
"""Local"""
# fruits_list_txt_files_folder_path = os.getcwd() + '/../supplier-data/descriptions/'

# URL of the server
## Replace <corpweb-external-IP> (35.222.215.76) with corpweb's external IP address.
"""Change me :) """
combat_server_url = 'http://34.133.106.182/fruits/'

list_dictionary_titles = ["title", "weight", "description", "image_name"]

# Get the list of all files and directories
# in the 'feedback_txt_files_folder_path' directory
print('======================')
print('----------------------')
print('# QA: Result: If everything is correct, it should return a list of TXT feedback files.')
print(os.listdir(fruits_list_txt_files_folder_path))
print('----------------------')

def change_TXT_files_2_automate_uploading(fruits_list_txt_files_folder_path):
    """1. Reading the contents of TXT files in a folder 'fruits_list_txt_files_folder_path'
       2. In weight, remove "lbs"
       3. Add the name of the image to the end of TXT"""

    # Get the list of all files and directories
    # in the 'fruits_list_txt_files_folder_path' directory
    print('======================')
    print('----------------------')
    print('# QA: Result: If everything is correct, it should return a list of TXT files.')
    print('# Difference from above: This test is already running from the "change_TXT_files_2_automate_uploading" function')
    print(os.listdir(fruits_list_txt_files_folder_path))
    print('----------------------')

    # Creating a variable for a list of TXT files
    txt_files_list = os.listdir(fruits_list_txt_files_folder_path)
    # QA: Iterating over each individual TXT file
    for file in txt_files_list:
        print(file + '    # QA : Iterating over each individual feedback file')

    print('----------------------')
    print('----------------------')
    print('# QA : Iterating over each individual feedback file content')
    print('# QA : The second line shows the converted dictionary')

    for file in txt_files_list:
        # https://ru.stackoverflow.com/questions/654183/%D0%9A%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D1%81%D1%82%D1%80%D0%BE%D1%87%D0%BA%D1%83-%D0%B2-txt-%D1%84%D0%B0%D0%B9%D0%BB%D0%B5-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-python-3
        # Remove "lbs"
        with open(fruits_list_txt_files_folder_path + file, 'r') as f:
            old_data = f.read()


        # What are we looking for and what are we changing at?
        new_data = old_data.replace(' lbs\n', '\n')
        with open(fruits_list_txt_files_folder_path + file, 'w') as f:
            f.write(new_data)
            print(file + "# Changed ' lbs' => ''")

    # Trying to write code that is reusable and won't add extra image names
    # https://stackoverflow.com/questions/44205923/checking-if-word-exists-in-a-text-file-python
    # search_word = input(image_name)
    # if search_word in open(fruits_list_txt_files_folder_path + file, 'a').read():
    #     print('# The script for changing the TXT file has been launched repeatedly')
    #     print('# "lbs" has already been removed from the TXT file')
    #     print('# Image title already added to TXT files')
    #     print('# No additional action required')
    #     pass
    # else:
    #     with open(fruits_list_txt_files_folder_path + file, 'a') as f:
    #         f.write('\n' + image_name)

    # https://www.geeksforgeeks.org/python-append-to-a-file/
    # Add to the end the name of the image file that matches the name of the TXT file
    for file in txt_files_list:
        with open(fruits_list_txt_files_folder_path + file, 'a') as f:
            image_name = file[:4] + "jpeg"
            # f.write('\n' + image_name)
            f.write(image_name)
            print(file + "# +name of the image")


# Modifying TXT files to automate downloads
# In weight, remove "lbs", add the name of the image to the end
change_txt_2_automate_uploading = change_TXT_files_2_automate_uploading(fruits_list_txt_files_folder_path)
