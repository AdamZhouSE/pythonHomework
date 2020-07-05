def arr33():
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    neg=[]
    pos=[]
    res=0
    for num in arr:
        if(num>=0):
            pos.append(num)
        else:
            neg.append(num)
    pos.sort()
    neg.sort(reverse=True)
    if(len(neg)%2==0):
        for i in range(0,len(neg)):
            res+=(-1-neg[i])
        for i in range(0,len(pos)):
            res+=abs(pos[i]-1)
    else:
        for i in range(1,len(neg)):
            res+=(-1-neg[i])
        res+=pos[0]-neg[0]
        for i in range(1,len(pos)):
            res+=abs(pos[i]-1)
    print(res)
    return 

arr33()