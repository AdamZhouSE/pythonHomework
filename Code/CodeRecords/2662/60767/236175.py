def getBinary(num):
    return '{:b}'.format(num)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    num = getBinary(test).count("1")
    if(num%2==0):
        print("even")
    else:
        print("odd")