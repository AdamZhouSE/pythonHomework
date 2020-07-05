def num(a,cc,k):
    x=[]
    for i in range(cc,k+1):
        x.append(a[i])
    return x
def sort(b,y):
    x=[]
    if y[0]==0:
        cc=y[1]-1
        k=y[2]-1
        for i in range(0, cc):
            x.append(b[i])
        d=num(b,cc,k)
        d.sort()
        for i in range(cc, k + 1):
            x.append(d[i-cc])
        for i in range(k + 1, len(b)):
            x.append(b[i])
    else:
        cc = y[1]-1
        k = y[2]-1
        for i in range(0, cc):
            x.append(b[i])
        d=num(b,cc,k)
        d.sort()
        for i in range(cc,k+1):
            x.append(d[k-i])
        for i in range(k + 1, len(b)):
            x.append(b[i])
    return x
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]=="," and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(" ")]
aa=str(input())
res=[int(x) for x in dele(aa).split(" ")]
xx=[]
for i in range(0,a[1]):
    aa = str(input())
    y = [int(x) for x in dele(aa).split(" ")]
    xx.append(y)
b=int(input())
for i in range(0,a[1]):
    res=sort(res,xx[i])
print(res[b-1])