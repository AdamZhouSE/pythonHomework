def exam3():
    t=int(input())
    for i in range(t):
        x=input().split(" ")
        a=int(x[0])
        b=int(x[1])
        n=int(input())
        d=b-a
        print(a+(n-1)*d)
exam3()