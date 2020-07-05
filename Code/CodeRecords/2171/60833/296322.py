for i in range(0,int(input())):
    count=int(input())
    s=list(map(int,input().split(' ')))
    even=[]
    odd=[]
    for j in s:
        if j%2:
            odd.append(j)
        else:
            even.append(j)
    res=even+odd
    for j in res:
        print(str(j),end=' ')
    print('')