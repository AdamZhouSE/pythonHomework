n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    water=0
    lower=min(a[0],a[-1])
    for i in range(1,m-1):
        if a[i]<lower:
            water+=(lower-a[i])
        else:
            lower=a[i]
    print(water)