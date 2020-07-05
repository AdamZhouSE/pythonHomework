def notS(n):
    if n==1:
        return 2
    elif n==2:
        return 3
    else:
        a=2
        b=3
        for i in range(n-1):
            a,b=b,a+b
        return a
t=eval(input())
for _ in range(t):
    n=eval(input())
    print(2**n-notS(n))