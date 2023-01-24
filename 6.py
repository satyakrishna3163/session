# How would you merge two sorted lists in Python

def Merge(ls1, ls2):
    merge_list = ls1 + ls2
    merge_list.sort()
    return(merge_list)
  

ls1 = [10,20,40,60,80,100]
ls2 = [11,22,33,44,55,66]
print(Merge(ls1, ls2))