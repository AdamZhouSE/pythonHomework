times=int(input())
def isPrime(n):
    if n==1 or n==0:
        return False
    if n==2:
        return True
    else:
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                return False
        return True

primeList=[]
for i in range(170):
    if isPrime(i):
        primeList.append(i)

def do(n,degree):
    if n==1 and degree==3:
        return 1
    for j in primeList:
        if n%j==0:
            n=n/j
            return do(n,degree+1)
    return 0
for i in range(times):
    print(do(int(input()),0))