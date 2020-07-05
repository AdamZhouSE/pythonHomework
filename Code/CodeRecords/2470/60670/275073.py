t=int(input())
for tt in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    print(n,a)
    for j in range(0,n):
        for i in range(n-1,-1,-1):
            print(a[i*3+j],end=' ')
    print()