t=int(input())
def f1(n):
    return (3*n-3)
def f2(n):
    if(n==2):
        return 5
    else:
        return f2(n-1)+f1(n)
def f3(n):
    if(n==1):
        return 3
    else:
        return f3(n-1)+f2(n)
for i in range(t):
    n=int(input())
    print(f3(n))