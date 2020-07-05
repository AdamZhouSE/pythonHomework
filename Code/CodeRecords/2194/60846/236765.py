import math

def isPrime(i):
    for j in range(2,math.floor(i**0.5)+1):
        if i%j==0:
            return False
    return i!=1

def findWithinRange(left,right):
    firstPrime=False
    for i in range(left,right+1):
        if isPrime(i) and not firstPrime:
            print(i,end='')
            firstPrime=True
        elif isPrime(i) and firstPrime:
            print('',i,end='')

n=int(input())
while n:
    line=input().split()
    findWithinRange(int(line[0]),int(line[1]))
    print()
    n-=1