import math

def getPrime(num):
    dis = []
    prime = 2
    while(num > 1 and prime <= math.sqrt(num)):
        if(num % prime == 0):
            num = num / prime
            dis.append(prime)
        else:
            prime = prime + 1
    if(num != 1):
        dis.append(int(num))
    return dis

n = int(input())
for i in range(0,n):
    num = int(input())
    expectation = getPrime(num)
    if(len(expectation) == 1):
        print(0)
    else:
        sumNum = sum(list(map(eval,str(num))))
        sumExp = 0
        for p in expectation:
            sumExp = sum(list(map(eval,str(p)))) + sumExp
        if(sumExp == sumNum):
            print(1)
        else:
            print(0)