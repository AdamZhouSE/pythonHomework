def a(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i])
    return res
n=int(input())
for p in range(n):
    count=0
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
                        if t==y:
                            count=count+1
    print(count)