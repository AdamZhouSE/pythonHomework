import math
def isPrime(n):
    if n<=1:
        return False
    i=2
    while i<int(math.sqrt(n))+1:
        if n%i==0:
            return False
        i+=1
    return True

n=int(input())
for i in range(n):
    number=int(input())
    
    count=0
    i=2
    while count<number:
        if isPrime(i):
            count+=1
            if count==number:
                break
        i+=1
    print(i**2+1)