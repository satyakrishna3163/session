import csv

file = open("C:\\Users\\lenovo\\Downloads\\CAT_Diagnostic_Test (2) 1.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)