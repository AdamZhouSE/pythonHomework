def cc(x,i,j,I,J):
    res=[]
    for l in range(i,I):
        xx=[]
        for p in range(j,J):
            xx.append(x[p])
        res.append(xx)
    return res
def x(a):
    res=[]
    for i in range(0,len(a)):
        res.append(a[i])
    return res
n=[int(x) for x in input().split(" ")]
c=[]
for i in range(n[0]):
    b=x(str(input()))
    c.append(b)
d=[]
for q in range(0,n[0]-1):
    for w in range(q+1,n[0]):
        for e in range(0,n[1]-1):
            for r in range(e+1,n[1]):
                if not cc(c,q,w,e,r) in d:
                    d.append(cc(c,q,w,e,r))
k=len(d)
print(k,end='')