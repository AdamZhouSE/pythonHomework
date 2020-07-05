import math
numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    temp = math.ceil(math.log(test,2))
    print(2**temp)

