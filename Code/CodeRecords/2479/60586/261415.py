def exam4():
    t=int(input())
    res=[]
    for i in range(t):
        a=list(input())
        b=list(input())
        for item in a:
            if b.count(item)==-1:
                res.append(item)
            res=list(set(res))
        for item in b:
            if a.count(item)==-1:
                res.append(item)
            res = list(set(res))
    s="".join(res)
    print(s)
exam4()