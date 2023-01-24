#How would you find the most frequent word in a text file in Python

from collections import Counter 
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print(word_count(r"C:\Users\lenovo\OneDrive\Documents\practice.txt"))
