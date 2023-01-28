#How would you list all files in a directory in Python

import os
path = r"C:\Users\lenovo\OneDrive\Documents"
dir_list = os.listdir(path)
print(path, "' :")
print(dir_list)