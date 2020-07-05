t=eval(input())
for _ in range(t):
    n=eval(input())
    a=1
    b=2
    for i in range(1,n):
        a,b=b,a+b;
    print(a)