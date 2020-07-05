T=int(input())
while T>0:
    n,k=map(int,input().split())
    num=[int(n) for n in input().split()]
    num=sorted(num)
    le=len(num)-1
    while k>0:
        if k==1:
            print(num[le],end=' \n')
            print
        else:
            print(num[le], end=' ')
        le-=1
        k-=1
    T-=1