def getBinary(num):
    return '{:b}'.format(num)

def decode(grayCode):
    res = []
    temp = grayCode[0]
    res.append(str(temp))
    for i in range(1,len(grayCode)):
        temp = temp^grayCode[i]
        res.append(str(temp))
    return "".join(res)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    s = getBinary(test)
    grayCode = []
    for i in s:
        grayCode.append(int(i))
    print(int(decode(grayCode),base=2))
