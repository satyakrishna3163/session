#How would you use the "filter" function in Python to extract all the even numbers from a list

lis1 = [1, 2, 3, 4, 5]
def is_even(x): 
    return x % 2 == 0
lis2 = list(filter(is_even, lis1))
print(lis2)