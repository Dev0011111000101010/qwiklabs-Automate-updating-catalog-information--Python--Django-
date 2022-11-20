#!/usr/bin/env python3

## Run in comand line BEFORE run the script
# sudo apt-get update
# sudo apt install python-django-common
# sudo systemctl start google-startup-scripts.service

import os
import requests
import json

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

## This folder stores TXT files feedback for the site
## The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
"""Online"""
fruits_list_txt_files_folder_path = '/home/student-00-0dd6461e8915/supplier-data/descriptions/'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
"""Local"""
# feedback_txt_files_folder_path = '/Users/il/PycharmProjects/Qwiklabs--Process-Text-Files-with-Python-Dictionaries-and-Upload-to-Running-Web-Service-using-Djang/test_feedback'

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


def txt_2_dictionary_jungo_structure(fruits_list_txt_files_folder_path):
    """1. Reading the contents of TXT files in a folder 'feedback_txt_files_folder_path'
       2. Convert content to dictionary using the correct names to upload to the site correctly"""

    # Get the list of all files and directories
    # in the 'fruits_list_txt_files_folder_path' directory
    print('======================')
    print('----------------------')
    print('# QA: Result: If everything is correct, it should return a list of TXT files.')
    print('# Difference from above: This test is already running from the "txt_2_dictionary_jungo_structure" function')
    print(os.listdir(fruits_list_txt_files_folder_path))
    print('----------------------')

    # Creating a variable for a list of TXT files
    txt_files_list = os.listdir(fruits_list_txt_files_folder_path)
    # QA: Iterating over each individual feedback file
    for file in txt_files_list:
        print(file + '    # QA : Iterating over each individual feedback file')

    print('----------------------')
    print('----------------------')
    print('# QA : Iterating over each individual feedback file content')
    print('# QA : The second line shows the converted dictionary')

    for file in txt_files_list:
        absolute_path_2_feedback = fruits_list_txt_files_folder_path
        with open(absolute_path_2_feedback + file) as f:
            # Hint on Loop Reading a File Line by Line
            # https://pythonru.com/osnovy/chtenie-iz-fajla-postrochno-v-python
            list_content_of_feedback_files = f.readlines()
            # list_content_of_feedback_files = f.readlines() + ', ' + file[:-3] + 'jpeg'
            print(list_content_of_feedback_files)
            # Hint: list to dictionary
            # https://careerkarma.com/blog/python-convert-list-to-dictionary/
            # fruits_list_dictionary = dict(zip(list_dictionary_titles, list_content_of_feedback_files))
            fruits_list_dictionary = dict(zip(list_dictionary_titles, list_content_of_feedback_files))
            print(fruits_list_dictionary)
            post_each_1_fruit_in_json_format_2_server = requests.post(combat_server_url, json=fruits_list_dictionary)
            print('======================')
            print('----------------------')
            print(' # QA: print(json.dumps(fruits_list_dictionary))')
            print(json.dumps(fruits_list_dictionary))
            print('----------------------')
            # Change single quotes in Python dictionary to Jason double quotes
            # It turned out to be mandatory for the manual addition of feedback and interfere with the automatic one
            # dictionary_double_quotes_formate_transform = json.dumps(fruits_list_dictionary)
            # post_each_1_feedback_in_json_format_2_server_double_quotes = requests.post(combat_server_url, json=dictionary_double_quotes_formate_transform)
            print('----------------------')
            print(' # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)')
            print(post_each_1_fruit_in_json_format_2_server)
            print('----------------------')
            print('')

    print('======================')
    print('----------------------')
    print(' # QA: response.status_code')
    print(post_each_1_fruit_in_json_format_2_server.status_code)
    print(' # QA: response.ok')
    print(post_each_1_fruit_in_json_format_2_server.ok)
    print('----------------------')
    print(' # QA: response.request.url')
    print(post_each_1_fruit_in_json_format_2_server.request.url)
    print('----------------------')
    print(' # QA: response.request.body')
    print(post_each_1_fruit_in_json_format_2_server.request.body)
    print('----------------------')
    print('')

# Launching the "txt_2_dictionary_jungo_structure" function into which the "fruits_list_txt_files_folder_path" path is passed
convert_txt_fruits_lis_2_dictionary_jungo_structure = txt_2_dictionary_jungo_structure(fruits_list_txt_files_folder_path)