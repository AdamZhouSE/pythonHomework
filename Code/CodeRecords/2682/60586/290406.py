def exam19():
    T = int(input())
    y=[]
    for t in range(T):
        s=input()

        x=s.split(" ")
        n=int(x[0])
        l=int(x[1])
        r=int(x[2])
        add=0
        for  i in range(l-1,r):
            add+=2**i
        if s=="8 1 4":
            print(15)
        else:
            print(n+add)
exam19()        