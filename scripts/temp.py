"""
chmod 600 ~/Downloads/qwiklabs-L36305267.pem
ssh -i ~/Downloads/qwiklabs-L36305267.pem student-00-5daf2a721226@34.135.109.205

0. Preparation for work
    ls ~/
    sudo chmod +x ~/download_drive_file.sh
    ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
    tar xf ~/supplier-data.tar.gz
    ls ~/supplier-data
    cat ~/supplier-data/descriptions/007.txt

1. Working with supplier images
    nano ~/changeImage.py
    sudo chmod +x ~/changeImage.py
    ./changeImage.py
    file ~/supplier-data/images/003.jpeg

Try NOT to install :)
    # Insurance for everything to work correctly
    #     sudo apt-get update
    #     sudo apt install python-django-common
    #     sudo systemctl start google-startup-scripts.service

Intermediate mandatory manual actions
    # Remove 1 Enter at end of file
    nano  ~/supplier-data/descriptions/010.txt
    # Remove 1 Enter at end of file
    nano  ~/supplier-data/descriptions/001.txt

2. Uploading images to web server
    Example
        [linux-instance-IP-Address]/upload URL
        cat ~/example_upload.py
        sudo chmod +x ~/example_upload.py
        ./example_upload.py
        [linux-instance-IP-Address]/media/images/
    Programmer's job
        nano ~/supplier_image_upload.py
        sudo chmod +x ~/supplier_image_upload.py
        ./supplier_image_upload.py

3. Uploading the descriptions
    Example
        linux-instance-IP-Address/fruits
        {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}
        http://[linux-instance-external-IP]/
        http://[linux-instance-external-IP]/fruits
        {"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
        http://[linux-instance-external-IP]/fruits
    Programmer's job ???1
        nano ~/run_first.py
        sudo chmod +x ~/run_first.py
        ./run_first.py
    Programmer's job ???2
        # Check if files have been modified correctly
        cat  ~/supplier-data/descriptions/010.txt
        cat  ~/supplier-data/descriptions/002.txt
        cat  ~/supplier-data/descriptions/001.txt
            nano ~/supplier-data/descriptions/001.txt
            nano ~/supplier-data/descriptions/002.txt
            nano ~/supplier-data/descriptions/003.txt
            nano ~/supplier-data/descriptions/004.txt
            nano ~/supplier-data/descriptions/005.txt
            nano ~/supplier-data/descriptions/006.txt
            nano ~/supplier-data/descriptions/007.txt
            nano ~/supplier-data/descriptions/008.txt
            nano ~/supplier-data/descriptions/009.txt
            nano ~/supplier-data/descriptions/010.txt


    Programmer's job ???3
        nano ~/run.py
        sudo chmod +x ~/run.py
        ./run.py

4. Generate a PDF report and send it through email
    4.1. Generate a PDF report and send it through email

        Try NOT to install :)
            # Insurance for everything to work correctly
                ## Run to correct work
                # pip install reportlab
                # pip install emails

        # Create a folder where the PDF is saved. Without creating a folder, the PDF cannot be saved.
        touch ~/tmp
        ls -l  ~/tmp
        ls -l  ~/
        nano ~/reports.py
        sudo chmod +x ~/reports.py
        ./reports.py
        ls -l  ~/
            # nano /tmp/reports.py
            # sudo chmod +x /tmp/reports.py
            # cd /tmp
            # ./reports.py


        nano ~/emails.py
        sudo chmod +x ~/report_email.py
        nano ~/report_email.py
        sudo chmod +x ~/report_email.py
        ./report_email.py

    4.2. Send report through email
        nano ~/report_email.py
        sudo chmod +x ~/report_email.py
        ./report_email.py

"""







