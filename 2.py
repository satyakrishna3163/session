#How would you check if a given string is a palindrome in Python

def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s = "python"
ans = isPalindrome(s)
if (ans):
    print("Yes")
else:
    print("No")