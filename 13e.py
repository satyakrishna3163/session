#How would you create a function in Python that takes a list of numbers as an argument and returns the sum of the even numbers in the list


def list_even(x):
    even = []
    for n in x:
        if not n %2:
            even.append(n)
    return even

numbers = [2,3,4,6,8,101,103,111,120,124]

print(list_even(numbers))