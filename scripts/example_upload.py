#!/bin/bash

# First parameter is the ID, second parameter is the filename
FILEID=$1
FILENAME=$2

# This script downloads the drive file with the given ID and saves it with the given name

COOKIE_FILE=$(mktemp cookiesXXXX.txt)

# First get the confirmation prompt because the file is too big
CONFIRM=$(wget --quiet --save-cookies ${COOKIE_FILE} --keep-session-cookies "https://docs.google.com/uc?export=download&id=${FILEID}" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')

# Then download the file using the confirmation prompt
wget --load-cookies ${COOKIE_FILE} "https://docs.google.com/uc?export=download&confirm=${CONFIRM}&id=${FILEID}" -O ${FILENAME}

# Finally, delete the cookie file
rm ${COOKIE_FILE}
student-00-8ffbbf494319@linux-instance:~$ cat example_upload.py
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})