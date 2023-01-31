# How would you find the second largest number in a list in Python

ls1 = [10, 20, 4, 45, 99,100,100]
ls2 = max(ls1)
ls3 = max(ls1, key=lambda x: min(ls1)-1 if (x == ls2) else x)
print(ls3)