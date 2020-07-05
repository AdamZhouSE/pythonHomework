T=int(input())
def isPrimeOne(num):
    oneCnt=0
    for i in range(32):
        if 1 & (num>>i) ==1: oneCnt+=1
    return isPrime(oneCnt)
import math
def isPrime(num):
    if num==1: return False
    isPrimeFlag=True
    for divisor in range(2,int(math.sqrt(num))+1):
        if num%divisor==0:
            isPrimeFlag=False
            break
    return isPrimeFlag
while T:
    nums=[int(x) for x in input().split()]
    primeCnt=0
    for num in range(nums[0],nums[1]+1):
        if isPrimeOne(num): primeCnt+=1
    print(primeCnt)
    T-=1