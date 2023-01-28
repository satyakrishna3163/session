#How would you rename a file in Python

import os
old_name = r"C:\Users\lenovo\OneDrive\Documents\practice.txt"
new_name = r"C:\Users\lenovo\OneDrive\Documents\practice_session.txt"
os.rename(old_name, new_name)
