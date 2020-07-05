def change(b,x):
    res=[]
    s=len(b)%x
    for i in range(x,len(b)):
        res.append(b[i])
    for i in range(0,x):
        res.append(b[i])
    return res
n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    d=int(input())
    x=change(b,d)
    cc=""
    for j in range(len(x)):
        cc=cc+str(x[j])
        cc=cc+" "
    print(cc)