def exam19():
    T = int(input())
    s=input()
    for t in range(T):
        x=s.split(" ")
        n=int(x[0])
        l=int(x[1])
        r=int(x[2])
        add=0
        for  i in range(l-1,r):
            add+=2**i
        print(n+add)
exam19()        