t=int(input())
for m in range(0,t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(0,n-k+1):
        maxn=0
        for j in range(i,i+k):
            if a[j]>maxn:
                maxn=a[j]
        print(maxn,end=' ')
    print()