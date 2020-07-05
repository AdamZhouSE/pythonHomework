def getSumofSquares(num):
    numStr=str(num)
    sum=0
    for i in numStr:
        sum += int(i)**2
    return sum

def isHappyNumber(num):
    while(True):
        num = getSumofSquares(num)
        if(num==1):
            return True
        if(num in [4,16,37,58,89,145,42,20]):
            return False

def getNext(num):
    num = num+1
    while(isHappyNumber(num) != True):
        num = num+1
    return num

numOfTests = int(input())
K = []
for x in range(0,numOfTests):
    K.append(int(input()))
result = []
for k in K:
    result.append(getNext(k))
for x in result:
    print(x)