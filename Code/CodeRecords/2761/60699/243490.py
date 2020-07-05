cnt=int(input())
for i in range(0,cnt):
    n=int(input())
    res=0
    for i in range(1,n+1):
        res+=(n+1-i)*(n+1-i)
    print(res)