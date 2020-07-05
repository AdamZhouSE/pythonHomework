def getBinary(num):
    return '{:08b}'.format(num)

def getPos(s1,s2):
    i = 7
    while(i>=0):
        if(s1[i]!=s2[i]):
            return (8-i)
        i= i-1

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(input().split())
for test in Tests:
    s1 = getBinary(int(test[0]))
    s2 = getBinary(int(test[1]))
    if(s1==s2):
        print(-1)
    else:
        print(getPos(s1,s2))