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
                    break
                if(m==0):
                    res.append(-1)
    for l in range(0,len(res)):
        print(res[l],end=" ")
    print()