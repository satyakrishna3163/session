#How would you use Python to open a file and read its contents line by line

with open(r"C:\Users\lenovo\OneDrive\Documents\text.txt") as f:
    lines = [line for line in f]
  
print(lines)