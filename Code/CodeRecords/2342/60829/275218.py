def change(b,x):
    res=[]
    k=0
    i=0
    while k<=len(b)-x:
        for i in range(k,x+k):
            res.append(b[2*k+x-1-i])
        k=k+x
    if not i==len(b)-1:
        for j in range(i,len(b)):
            res.append(b[len(b)-1+i-j])
    return res
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    x=change(b,a[1])
    print(str(b)+" "+str(a[1]))
    cc=""
    for j in range(len(x)):
        cc=cc+str(x[j])
        if not j==len(x)-1:
            cc=cc+" "
    print(cc)