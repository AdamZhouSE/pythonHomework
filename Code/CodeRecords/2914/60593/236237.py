t=int(input())
for tt in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    beg=-1
    for i in range(n):
        if(a[i]!=b[i]):
            beg=i
            dd=a[i]-b[i]
            break
    for i in range(n-1,-1,-1):
        if(a[i]!=b[i]):
            ed=i
            break
    if(beg==-1):
        print('YES')
    else:
        if(beg==ed):
            print('NO')
        else:
            flag=True
            for i in range(beg+1,ed):
                if(a[i]-b[i]!=dd):
                    flag=False
            print('YES'if flag else'NO')