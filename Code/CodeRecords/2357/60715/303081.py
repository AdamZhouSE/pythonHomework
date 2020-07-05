T=int(input())
while T>0:
    n,m,x=map(int,input().split())
    a=[int(n) for n in input().split()]
    b=[int(n) for n in input().split()]
    for i in a:
        for j in b:
            if i+j==x:
                print(i,end=' ')
                print(j)
    T-=1