def change(b,x):
    res=[]
    k=(len(b)-len(b)%x)//x
    for d in range(0,k):
        for i in range(d*x,x+d*x):
            res.append(b[2*x*d+x-1-i])
        k=k+x
    dd=len(b)-len(b)%x
    if not dd==len(b):
        for j in range(dd,len(b)):
            res.append(b[len(b)-1+dd-j])
    return res
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    x=change(b,a[1])
    cc=""
    for j in range(len(x)):
        cc=cc+str(x[j])
        cc=cc+" "
    print(cc)