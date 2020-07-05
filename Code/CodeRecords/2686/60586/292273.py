def exam22():
    T=int(input())
    for t in range(T):
        n=int(input())
        if n<10:
            print(n*10**n)
        else:
            x=n//9
            y=n%9
            a=0
            for i in range(x):
                a =9*10**i+a
            a=a+y*10**x
            print(a*10**n)
exam22()
