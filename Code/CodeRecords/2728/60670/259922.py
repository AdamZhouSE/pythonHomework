t=int(input())
for k in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    maxn=0
    for i in range(0,n):
        for j in range(i+1,n):
            tmp=(j-i)*min(a[i],a[j])
            if tmp>maxn:
                maxn=tmp
    print(maxn)