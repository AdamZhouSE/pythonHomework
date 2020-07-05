def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def factorial(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t

n=int(input())
numOfPrime=0
for i in range(2,n+1):
    if isPrime(i):
        numOfPrime+=1
print((factorial(numOfPrime)*factorial(n-numOfPrime))%1000000007)