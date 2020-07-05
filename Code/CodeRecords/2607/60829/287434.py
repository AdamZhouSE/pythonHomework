def a(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i])
    res.sort()
    return res
n=int(input())
for p in range(n):
    count=0
    s=a(str(input()))
    for q in range(0,len(s)-1):
        for w in range(q+1,len(s)):
            for e in range(0,len(s)-1):
                for r in range(e+1,len(s)):
                    if not q==w and a(s[q:w+1])==a(s[e:r+1]):
                        count=count+1
    print(count)