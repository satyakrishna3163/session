

 #How would you check the size of a file in Python

import os
def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return (file_info.st_size)
file_path = r"C:\Users\lenovo\OneDrive\Documents\text.txt"
print (file_size(file_path),"mb")