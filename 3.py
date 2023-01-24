#How would you reverse a string in Python?

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str 
s = "krishna" 
print(end="")
print(reverse(s))