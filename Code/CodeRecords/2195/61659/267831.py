import math


def turnToBinary(x):
    result = ""
    while x != 0:
        remain = x % 2
        x = int(math.floor(x / 2))
        result = str(remain) + result
    return result

def isPrime(x):
    if x==1 or x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

T=int(input())
for i in range(0,T):
    temp=list(input().split(" "))
    start=int(temp[0])
    end=int(temp[1])
    res=0

    for i in range(start,end+1):
        string=turnToBinary(i)
        if isPrime(string.count("1")):
            res=res+1
    print(res)