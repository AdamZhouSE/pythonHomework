def getSum(num):
    return int((num+1)*num/2)

def getNth(num):
    start = getSum(num-1)+1
    result = 1
    for i in range (start,start+num):
        result = result*i
    return result

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    result = 0
    for i in range(1,test+1):
        result = result + getNth(i)
    print(result)