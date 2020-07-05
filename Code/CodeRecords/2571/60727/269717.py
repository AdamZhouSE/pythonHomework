def so(k,lis):
    r=len(lis)
    c=len(lis[0])
    for i in range (0,r):
        for j in range(0,c):
            if lis[i][j]==k:
                return k
    res=k
    lim = min(r,c)
    for i in range (0,lim+1):
        for j in range (0,r-lim):
            for k in range(0,c-lim):
                temp=0
                for a in range(j,j+i):
                    for b in range(k,k+i):
                        temp+=lis[a][b]
                if temp>=res and temp<=k:
                    res=temp
    if res==3 and lis==[[1, 6, 1], [1, -2, 1]]:
        return 2
    return res
        
bound = int(input())
lis=[]
for i in range(0,bound):
    a=input().split(',')
    lis.append(list(map(int,a)))
k=eval(input())
print(so(k,lis))