def exam6():
    t=int(input())
    for i in range(t):
        p=[1,1,1]
        n=int(input())
        for j in range(3,n+1):
            x=p[j-2]+p[j-3]
            p.append(x)
        print(p[n])
exam6()