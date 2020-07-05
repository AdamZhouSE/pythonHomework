t=int(input())
for k in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    maxn=0
    for i in range(0,n):
        wide=1
        for j in range(i+1,n):
            if a[j]<a[i]:
                break
            wide+=1
        for j in range(i-1,0,-1):
            if a[j]<a[i]:
                break
            wide+=1
        if a[i]*wide>maxn:
            maxn=a[i]*wide
    print(maxn)