T = int(input())
for i in range(T):
    LENGTH = int(input())
    numList = [int(x) for x in input().split()]
    res = []
    for j in range(LENGTH):
        if(j==LENGTH-1):
            res.append(-1)
        else:
            for m in range(j+1,LENGTH):
                if(numList[m]>=numList[j]):
                    res.append(numList[m])
                    break
                if(m==LENGTH-1):
                    res.append(-1)
    for t in range(LENGTH-1):
        print(res[t],end=" ")
    print(res[LENGTH-1])
    # if(res==[-1,4,4,-1]):
    #     print(numList)