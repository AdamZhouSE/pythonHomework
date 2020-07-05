def f(n):
    if n==0 or n==1 or n==2:
        return 1
    return f(n-2)+f(n-3)


T=int(input())
for i in range(0,T):
    n=int(input())
    print(f(n))