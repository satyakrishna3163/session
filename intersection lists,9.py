def intersection_list(list1,list2):
    list3 =[value for value in list1 if value in list2]
    return list3
list1 =[10,20,30,40,56,36,48]
list2 =[2,3,20,56,36,30,44,88]
print(intersection_list(list1, list2))