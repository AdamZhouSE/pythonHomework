def judge(n):
    t='true'
    f='false'
    n=list(n)
    length=len(n)
    store=[]
    m=''
    for i in range(37):
        m=str(2**i)
        if len(m)==length:
            store.append(m)
    midlist=[]
    n=list(n)
    j=0
    for v in store:
        midlist=list(v)
        for i in range(10):
            if n.count(str(i))==midlist.count(str(i)):
                j=j+1
                continue
            else:
                j=0
                break
        if j==10:
            break
    if j==10:
        print(t)
    else:
        print(f)
            
n=str(input())
judge(n)