def tree10():
    line1=input().split(' ')
    N,M=int(line1[0]),int(line1[1])
    houses=[]
    cows=[]
    res=0
    for i in range(N):
        houses.append(int(input()))
    for i in range(M):
        str=input()
        if(str[-1]==' '):
            str=str[:len(str)-1]
        cows.append([int(x) for x in str.split(' ')])
    cows.sort(key=lambda x:x[1])
    for i in range(M-1):
        if(cows[i][1]==cows[i+1][1] and cows[i][1]-cows[i][0]>cows[i+1][1]-cows[i+1][0]):
            cows[i],cows[i+1]=cows[i+1],cows[i]
    tmp=[0]*N
    for row in cows:
        empty=True
        for i in range(row[0]-1,row[1]):
            if tmp[i]+1>houses[i]:
                empty=False
        if(empty):
            for i in range(row[0] - 1, row[1]):
                tmp[i]+=1
            res+=1
    print(res)
    return


tree10()