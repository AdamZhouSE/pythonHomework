import math
def check(n):
    isPrime=True
    for i in range(2,n):
        if n%i==0:
            isPrime=False
            break
    return isPrime

n=int(input())
count=0
for i in range(2,n+1):
    if check(i):
        count+=1
print(math.factorial(count)*math.factorial(n-count)%(1000000007))