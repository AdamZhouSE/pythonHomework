T=int(input())
for i in range(0,T):
    n,m=(map(int ,input().split(" ")))
    lis=list(map(int ,input().split(" ")))
    for j in range(m-1,n):
        a=0
        for k in range(0,m):
            a=max(a,lis[j-k])
        print(a,end=" ")
    print()  