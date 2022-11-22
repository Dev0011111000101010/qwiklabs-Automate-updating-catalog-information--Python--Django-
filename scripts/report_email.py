#!/usr/bin/env python3

# pip install emails
import emails
import os

# Example from https://github.com/Dev0011111000101010/qwiklabs.com-Automatically-Generate-a-PDF-and-send-it-by-Email-Python/blob/main/scripts/example.py
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(message)

