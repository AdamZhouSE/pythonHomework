import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n=int(input())
cnt=0
for i in range(2,n):
    if isPrime(i): cnt+=1
print(cnt)
