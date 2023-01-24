# How would you find the most common element in a list in Python


import statistics
from statistics import mode
def most_common(List):
    return (mode(List))
 
List = [10,30,20,10,20,10,10,12,20,20]
print(most_common(List))