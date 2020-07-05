K=int(input())
if K%2==0 or K%5==0 :
    print(-1)
else:
    n=1
    r=int("1"*n)
    while r%K!=0:
        n=n+1
        r=int("1"*n)
    print(n)