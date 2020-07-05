def f(n):
    if n==1:
        return 2
    if n==2:
        return 3
    return f(n-1)+f(n-2)


T=int(input())
for i in range(0,T):
    n=int(input())
    print(f(n))