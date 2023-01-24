# How would you find the second largest number in a list in Python

def method1(arr):
    arr.sort() 
    print(arr[-2])

print(method1(arr=[10,40,60,70,90,76]))