def ferb(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        fn2=1
        fn1=2
        fn=0
        for i in range(2,n):
            fn=fn2+fn1
            fn2=fn1
            fn1=fn
        return fn
        
T=int(input())
for i in range(0,T):
    n=int(input())
    re=ferb(n)
    print(re)
