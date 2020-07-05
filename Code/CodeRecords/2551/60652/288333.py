N,M=map(int,input().split())
l=[0]*N
for i in range(M):
    c,a,b=map(int,input().split())
    if c==0:
        for index in range(a-1,b):
            if l[index]==1:
                l[index]=0
            else:
                l[index]=1
    else:
        print(l[a-1:b].count(1))