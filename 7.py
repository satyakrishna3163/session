def checkPrime(x):
    for i in range(2, x):
        if n%i==0:
            return 1

print("Enter a Number: ", end="")
n = int(input())

p = checkPrime(n)
if p==1:
    print(str(n)," is not a Prime Number")
else:
    print(str(n), " is a Prime Number")