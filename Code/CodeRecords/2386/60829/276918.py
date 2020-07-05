n=int(input())
for p in range(n):
    x=int(input())
    b=[int(x) for x in input().split(" ")]
    c=int(input())
    res=[]
    for i in range(0,len(b)-3):
        for j in range(i+1,len(b)-2):
            for k in range(j+1,len(b)-1):
                for l in range(k+1,len(b)):
                    if b[i]+b[j]+b[k]+b[l]==c:
                        d=[]
                        d.append(b[i])
                        d.append(b[j])
                        d.append(b[k])
                        d.append(b[l])
                        res.append(d)
    res1=[]
    for i in res:
        if not i in res1:
            res1.append(i)
    if len(res1)>0:
        print(1)
    else:
        print(0)