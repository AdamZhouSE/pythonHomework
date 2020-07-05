def exam19():
    T = int(input())
    for t in range(T):
        x=input().split(" ")
        n=int(x[0])
        l=int(x[1])
        r=int(x[2])
        print(n+2**(l-1)+2**(r-1))
exam19()        