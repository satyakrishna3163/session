#How would you zip and unzip files in Python

from zipfile import ZipFile
with ZipFile(r"C:\Users\lenovo\OneDrive\Documents\practice_session 1.zip", 'r') as zObject:
    zObject.extractall(
        path=r"C:\Users\lenovo\OneDrive\Documents")