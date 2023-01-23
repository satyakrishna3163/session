def most_frequent(List):
    return max(set(List), key = List.count)
 
List = [10,30,20,10,20,10,10,12]
print(most_frequent(List))