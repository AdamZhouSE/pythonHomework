T=int(input())
for o in range(0,T):
    n=int(input())
    lis=list(map(int ,input().split(" ")))
    re=0
    for i in range(1,n+1):
        for j in range(0,n):
            if(j+i>n):
                break
            if(i==1):
                if(lis[j]>re):
                    re=lis[j]
            else:
                a=0
                for k in range(j+1,j+i):
                    a=int(min(lis[k-1],lis[k]))
                if(i*a>re):
                    re=i*a
    print(re)