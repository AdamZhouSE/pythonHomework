def exam6():
    t=int(input())
    p=[1,1,1]
    for i in range(t):
        n=int(input())
        for j in range(3,n+1):
            x=p[j-2]+p[j-3]
            p.append(x)
        print(p[n])
exam6()