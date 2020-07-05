def getBinary(num):
    return '{:08b}'.format(num)

def switch(binStr):
    temp = list(binStr)
    odd = temp[0::2]
    even = temp[1::2]
    result = []
    if(len(temp)%2==0):
        for i in range(0,len(even)):
            result.append(even[i])
            result.append(odd[i])
        return (result)
    else:
        result.append(odd[0])
        for i in range(1,len(odd)):
            result.append(odd[i])
            result.append(even[i-1])
        return (result)

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for test in Tests:
    print(int("".join(switch(getBinary(test))),base=2))


