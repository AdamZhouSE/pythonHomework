def getBinary(num):
    return '{:b}'.format(num)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    s = getBinary(test)
    a = s.count("0")
    b = s.count("1")
    print(a^b)