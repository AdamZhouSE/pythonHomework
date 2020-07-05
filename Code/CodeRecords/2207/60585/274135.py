def F(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res

t=eval(input())
for _ in range(t):
    arr=list(map(int,input().strip().split(' ')))
    n=arr[0]
    m=arr[1]
    if n>=F(m):print(1)
    else:print(0) 