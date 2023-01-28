#How would you read a file in binary mode in Python?

with open(r"C:\Users\lenovo\OneDrive\Documents\text.txt", mode="rb") as text_file:
    co = text_file.read()
print(co)