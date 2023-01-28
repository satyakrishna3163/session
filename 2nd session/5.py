#How would you check if a file is open or closed in Python

import os

def check_file_status(self):
    try:
        os.rename(r"text.txt", r"text.txt")
        print("File is closed.")
    except OSError:
        print("File is opened.")
print(check_file_status)