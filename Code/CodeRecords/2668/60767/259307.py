def getBinary(num):
    return '{:b}'.format(num)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    binStr = getBinary(test)
    a = binStr.replace("0","x")
    b = a.replace("1","0")
    c = b.replace("x","1")
    print(int(c,base=2),"",end='')
    print(test+int(c,base=2))