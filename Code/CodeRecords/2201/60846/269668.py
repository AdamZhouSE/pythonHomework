import math
def isPrime(num):
    if num==1: return False
    isPrimeFlag=True
    for divisor in range(2,int(math.sqrt(num))+1):
        if num%divisor==0:
            isPrimeFlag=False
            break
    return isPrimeFlag
t=int(input())
while t:
    twoNums=[int(x) for x in input().split()]
    twoSum=sum(twoNums)
    minPen=1
    while not isPrime(twoSum+minPen):
        minPen+=1
    print(minPen)
    t-=1