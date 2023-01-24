#How would you use the "zip" function in Python to combine two lists element-wise

import itertools
  
list_1 = [[1, 3], [4, 5], [5, 6]]
list_2 = [[11, 9], [16, 2], [4, 10]]
res = [list(itertools.chain(*i)) 
       for i in zip(list_1, list_2)]
      
print(res)