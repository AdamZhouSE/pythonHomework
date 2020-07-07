t=int(input())
while t>0:
    n=int(input())
    num=list(map(int,input().split()))
    mxind=-1
    maxrep=1
    for i in range(0,n):
        no=num.count(num[i])
        if no>1:
            maxrep=no
            mxind=i
            break
    if maxrep==1:
        print(-1)
    else:
        print(mxind+1)
    t=t-1