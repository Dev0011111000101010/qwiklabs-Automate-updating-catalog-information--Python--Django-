#!/usr/bin/env python3

"""This script creates a PDF file"""

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

""" In an attempt to overcome the error AttributeError: module 'reports' has no attribute 'generate'
    # https://stackoverflow.com/questions/59762996/how-to-fix-attributeerror-partially-initialized-module
    filename changed from "reports.py" => "re_ports_1.py" """

import os
from datetime import date

# https://youtu.be/ZDR7-iSuwkQ
# creting PDF file
from reportlab.pdfgen import canvas

# This folder stores TXT files for PDF
# The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
"""Online"""
fruits_list_txt_files_folder_path = os.getcwd() + '/supplier-data/descriptions/'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
"""Local"""
# fruits_list_txt_files_folder_path = os.getcwd() + '/../supplier-data/descriptions/'

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
            # data_4_report = 'name: ' + fruits_list_dictionary['name'][:-1] + '\n' +  'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs' + '\n'
            # data_4_report = 'name: ' + fruits_list_dictionary['name'][:-1] + "'<br/>'" +  'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs' + "'<br/>'"
            # data_4_report = 'name: ' + fruits_list_dictionary['name'][:-1] + ', ' +  'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs' + ', '

            data_4_report_1 = 'name: ' + fruits_list_dictionary['name'][:-1]
            data_4_report_2 = 'weight: ' + fruits_list_dictionary['weight'][:-1] + ' lbs'
            data_4_report_3 = ''

            summary_for_PDF.append([data_4_report_1])
            summary_for_PDF.append([data_4_report_2])
            summary_for_PDF.append([data_4_report_3])


    print('======================')
    print('----------------------')
    print('# summary_for_PDF')
    print(summary_for_PDF)
    print('----------------------')
    print('')

    return summary_for_PDF

def create_PDF(fruits_list_txt_files_folder_path):
    """Creates PDF file
        Script to generate a PDF report"""

    """ In an attempt to overcome the error AttributeError: module 'reports' has no attribute 'generate'
        # https://stackoverflow.com/questions/1250103/attributeerror-module-object-has-no-attribute
        import moved inside function """

    gathering_data_4_PDF_file_creation = create_data_4_PDF(fruits_list_txt_files_folder_path)

    print('======================')
    print('----------------------')
    print('# summary_for_PDF')
    print('# def create_PDF(fruits_list_txt_files_folder_path):')
    print(summary_for_PDF)
    print('----------------------')
    print('')



    print("I'm here")

    # https://youtu.be/ZDR7-iSuwkQ
    # creting PDF file
    file_name = 'processed.pdf'

    # Save to picked location
    # https://stackoverflow.com/questions/14778256/reportlab-save-location
    scripts_absolute_path = os.getcwd()
    print(scripts_absolute_path)
    pdf_file_folder_reletive_path = '/tmp/'
    # The code caused an error when used
    # NotADirectoryError: [Errno 20] Not a directory: '/home/student-00-5daf2a721226/tmp/processed.pdf'
    # pdf_file_absolute_path = scripts_absolute_path + pdf_file_folder_reletive_path
    pdf_file_absolute_path = '/tmp/'
    pdf_file_absolute_path_and_file_name = os.path.join(pdf_file_absolute_path, file_name)
    print(pdf_file_absolute_path)
    print(pdf_file_absolute_path_and_file_name)

    document_title = 'document_title: Processed Update on'
    title_1_part = 'Processed Update on'
    # https://www.programiz.com/python-programming/online-compiler/?ref=e0b9489a
    today = date.today()
    title_2_part = today.strftime("%B %d, %Y")
    print(title_2_part + "    #QA: 'title_2_part'")
    title = title_1_part + ' ' + str(title_2_part)
    print(title + "    #QA: 'title' = title_1_part + ' ' + str(title_2_part)")
    text_lines = summary_for_PDF
    # File name + path
    # The code caused an error when used
    # NotADirectoryError: [Errno 20] Not a directory: '/home/student-00-5daf2a721226/tmp/processed.pdf'
    pdf = canvas.Canvas(pdf_file_absolute_path_and_file_name)
    # pdf = canvas.Canvas(file_name)

    # Document title
    pdf.setTitle(document_title)
    # Title
    pdf.drawCentredString(297, 770, title)
    # Text (big data, many rows)
    text = pdf.beginText(40, 730)
    for line in text_lines:
        print(text_lines)
        print(line)
        text.textLines(line)

    pdf.drawText(text)

    # Save PDF to chosen PATH ("pdf_file_absolute_path_and_file_name")
    pdf.save()

creating_PDF_file = create_PDF(fruits_list_txt_files_folder_path)