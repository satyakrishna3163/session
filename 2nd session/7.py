#How would you move the pointer to a specific position in a file in Python

with open(r"C:\Users\lenovo\OneDrive\Documents\text.txt", "r") as fp:
    fp.seek(12)
    print(fp.read())