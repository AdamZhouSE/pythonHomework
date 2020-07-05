t=int(input())
def split(n):
    a=n//2
    b=n//3
    c=n//4
    if (a+b+c)<=n:
        return n
    else:
        return split(a)+split(b)+split(c)
for i in range(t):
    n=int(input())
    print(split(n))