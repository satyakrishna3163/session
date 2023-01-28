#How would you create a new directory in Python

import os  
directory = "krishna file" 
parent_dir = r"D:\ksdpjsdp"
path = os.path.join(parent_dir, directory) 
os.makedirs(path) 
print(directory) 