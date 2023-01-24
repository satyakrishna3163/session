# How would you use the "map" function in Python to square all the elements in a list

def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
result = map(square_num, nums)
print(list(result))