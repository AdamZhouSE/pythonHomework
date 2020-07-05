def isPrime(num):
    if(num==1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def getNextPrime(num):
    num=num+1
    while(isPrime(num)!=True):
        num = num+1
    return num
numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for test in Tests:
    a = int(test[0])
    b = int(test[1])
    print(getNextPrime(a+b)-(a+b))