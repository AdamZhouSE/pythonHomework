def getSum(num):
    return int((num+1)*num/2)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for test in Tests:
    target = int(test[0])
    num = int(test[1])
    if(getSum(num)>target):
        print(0)
    else:
        print(1)