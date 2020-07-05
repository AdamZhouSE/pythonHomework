def arr43():
    n=int(input())
    for i in range(n):
        line1=input().split(' ')
        lenx,leny=int(line1[0]),int(line1[1])
        X=[int(x) for x in input().split(' ')]
        
        Y = [int(x) for x in input().split(' ')]
        res=0
        for j in range(lenx):
            for k in range(leny):
                if(X[j]**Y[k]>Y[k]**X[j]):
                    res+=1
        print(res)
    return

arr43()