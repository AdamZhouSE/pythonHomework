numOfTests = int(input())
Tests = []
arr = []
for i in range(0,numOfTests):
    Tests.append(input().split())
    arr.append(input().split())
for i in range(0,numOfTests):
    len = int(Tests[i][0])
    redix = int(Tests[i][1])
    temp = 0
    for x in range(0,len):
        if(int(arr[i][x])%redix==0):
            temp = temp|int(arr[i][x])
    print(temp)