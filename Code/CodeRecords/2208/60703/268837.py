T  = int(input())
for i in range(T):
    n = int(input())
    numList = [int(x) for x in input().split()]
    res = []
    for j in range(n):
        if(j==0):
            res.append(-1)
        else:
            for m in range(j-1,-1,-1):
                if(numList[m]<numList[j]):
                    res.append(numList[m])
                    continue
                if(j-1==0):
                    res.append(-1)
    for l in range(0,len(res)-1):
        print(res[l],end=" ")
    print(res[-1])