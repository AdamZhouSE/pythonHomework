def exam26():
    T=int(input())
    for t in range(T):
        x=input().split(" ")
        m=list(x[0])
        n=list(x[1])
        string=list(set(m+n))
        print(len(string))
exam26()