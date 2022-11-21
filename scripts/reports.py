#!/usr/bin/env python3

"""This script creates a PDF file"""

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

import os

# This folder stores TXT files for PDF
# The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
"""Online"""
# fruits_list_txt_files_folder_path = os.getcwd() + '/supplier-data/descriptions/'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
"""Local"""
fruits_list_txt_files_folder_path = os.getcwd() + '/../supplier-data/descriptions/'

list_dictionary_titles = ["name", "weight", "description", "image_name"]

summary_for_PDF = []
def create_data_4_PDF(fruits_list_txt_files_folder_path):
    """This script creates data for creating the PDF file
        data is taken from TXT files by PATH "fruits_list_txt_files_folder_path"
        gathering in "summary_for_PDF"
        Script to generate a PDF report"""

    print('======================')
    print('----------------------')
    print('# QA: if the PATH is visible, then the PATH to the folder with TXT files is correctly built')
    print(fruits_list_txt_files_folder_path)
    print('----------------------')
    print('')

    # Get the list of all files and directories
    # in the 'fruits_list_txt_files_folder_path' directory
    print('======================')
    print('----------------------')
    print('# QA: Result: If everything is correct, it should return a list of TXT files.')
    print('# Difference from above: This test is already running from the "create_PDF_file" function')
    print(os.listdir(fruits_list_txt_files_folder_path))
    print('----------------------')
    print('')

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
        absolute_path_2_feedback = fruits_list_txt_files_folder_path
        with open(absolute_path_2_feedback + file) as f:
            # Hint on Loop Reading a File Line by Line
            # https://pythonru.com/osnovy/chtenie-iz-fajla-postrochno-v-python
            list_content_of_feedback_files = f.readlines()
            # list_content_of_feedback_files = f.readlines() + ', ' + file[:-3] + 'jpeg'
            print(list_content_of_feedback_files)

            # Hint: list to dictionary
            # https://careerkarma.com/blog/python-convert-list-to-dictionary/
            fruits_list_dictionary = dict(zip(list_dictionary_titles, list_content_of_feedback_files))
            print(fruits_list_dictionary)

            # Report template
            print('name: ' + fruits_list_dictionary['name'][:-1] + '\n' +  'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs' + '\n')
            data_4_report = 'name: ' + fruits_list_dictionary['name'][:-1] + '\n' +  'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs' + '\n'
            summary_for_PDF.append(data_4_report)

    print('======================')
    print('----------------------')
    print('# summary_for_PDF')
    print(summary_for_PDF)
    print('----------------------')
    print('')

def create_PDF():
    """Creates PDF file
        Script to generate a PDF report"""
    ## Online version of the path
    reports.generate("/tmp/report.pdf", "Sales summary for last month", pdf_join_summary, data_for_PDF_report)
    ## Local version of the path
    # reports.generate("/Users/il/PycharmProjects/qwiklabs.com-Automatically-Generate-a-PDF-and-send-it-by-Email-Python/scripts/report.pdf", "Sales summary for last month", pdf_join_summary, data_for_PDF_report)


gathering_data_4_PDF_file_creation = create_data_4_PDF(fruits_list_txt_files_folder_path)
# creating_PDF_file = create_PDF()