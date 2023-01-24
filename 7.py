# How would you check if a given number is prime in Python


num = int(input("enter the number"))
def is_prime(num): 
    if(num <= 1): 
        return False
    for i in range(2,num): 
        if (num % i) == 0:
            return False 
    return True 
if (is_prime(num)): 
    print(num,"is a prime number") 
else: 
    print(num,"is not a prime number")