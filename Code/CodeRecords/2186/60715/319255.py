t=int(input())
for i in range(t):
    n=int(input())
    res=0
    for m in range(n):
        res+=((n-m)*(m+1))
    print(res)