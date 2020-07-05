def getMax(windowSize,arr):
    length = len(arr)
    max = -10000000
    for i in range(0,length-windowSize+1):
        min = 100000000000000
        for x in range(0,windowSize):
            if(int(arr[x+i])<min):
                min = int(arr[x+i])
        if(min>max):
            max = min
    return max

numOfTests = int(input())
Tests = []
l = []
for i in range(0,numOfTests):
    l.append(int(input()))
    Tests.append(input().split())
for i in range(0,numOfTests):
    for x in range(1,l[i]):
        print(getMax(x,Tests[i]),"",end="")
    print(getMax(l[i],Tests[i]))


