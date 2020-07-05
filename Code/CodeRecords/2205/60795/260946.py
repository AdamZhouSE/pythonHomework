def fx(n):
    if n==1 or n==0:
        return 1
    else:
        x=0
        for i in range(0,n):
            x=x+fx(n-1-i)*fx(i)
        return x
T=int(input())
for i in range(0,T):
    n=int(input())
    num=n//2
    x=fx(num)
    print(x)