def f(n,d):
    if d == 0:
        return 1
    return f(n,d-1)**n+1

n,d = map(int,input().split(" "))
print(f(n,d)-f(n,d-1),end="")