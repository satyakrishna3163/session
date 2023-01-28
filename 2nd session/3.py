#How would you read a specific line from a file in Python?

import linecache

line_numbers = [3]
lines = []
for i in line_numbers:
    x = linecache.getline(r"C:\Users\lenovo\OneDrive\Documents\text.txt", i)
    lines.append(x)
print(lines)