

def getList(num):
    L = []
    L.append(num)
    temp = num
    while(temp > 0):
        temp = temp-5
        L.append(temp)
    while(temp != num):
        temp = temp+5
        L.append(temp)
    return L

def present(l):
    for num in l:
        print(num,"",end='')
    print()

numOfTests = int(input())
Tests = []
for i in range(0,numOfTests):
    Tests.append(int(input()))
for x in Tests:
    present(getList(x))