t=int(input())
for tt in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    print(n,a)
    for i in range(n-1,-1,-1):
        for j in range(0,n):
            print(a[i*3+j],end=' ')
    print()