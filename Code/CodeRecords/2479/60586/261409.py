def exam4():
    t=int(input())
    res=[]
        for i in range(t):
        a=list(input())
        b=list(input())
        for item in a:
            if b.count(item)==-1:
                res.append(item)
            list=list(set(list))
        for item in b:
            if a.count(item)==-1:
                res.append(item)
            list = list(set(list))
    s="".join(res)
    print(s)
exam4()