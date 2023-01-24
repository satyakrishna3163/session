#How would you use the "reduce" function from the "functools" module in Python to find the product of all the elements in a list

from functools import reduce

def sum(a, b):
    print(f"{a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)
