def a(x):
    res=[]
    for i in range(len(x)):
        res.append(int(x[i]))
    return res
def judge(x):
    res=[]
    for i in x:
        if not i in res:
            res.append(i)
    if res==[0,1,2]:
        return True
    else:
        return False
n=int(input())
for p in range(n):
    count=[]
    s=a(str(input()))
    print(s)
    for q in range(0,len(s)-1):
        for w in range(q+1,len(s)):
            for e in range(0,len(s)-1):
                for r in range(e+1,len(s)):
                    if not q==w :
                        t=s[q:w+1]
                        y=s[e:r+1]
                        t.sort()
                        y.sort()
                        if t==y and judge(t) :
                            count.append(t)
    aa=[]
    bb=[]
    print(s)
    