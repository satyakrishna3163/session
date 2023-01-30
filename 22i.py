# How would you use the "itertools" module in python to find all possible permutations of a given list

from itertools import permutations

a = "1234"
p = permutations(a)
for j in list(p):
  print(j)