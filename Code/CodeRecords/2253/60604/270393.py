x=input().split()
n=int(x[0])
m=int(x[1])
a=input().split()
for i in range(n):
    a[i]=int(a[i])
for I in range(m):
    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    print(x)
    if x[0]==3:
        pos=x[1]+1
        a[pos]=x[2]
    else:
        l=x[1]-1
        r=x[2]
        tmp=x[l:r]
        res=0
        if x[0]==1:
            tmp.sort()
            for i in range(len(tmp)):
                if tmp[i]==x[3]:
                    res=i+1
        elif x[0]==2:
            tmp.sort()
            res=tmp[x[3]-1]
        elif x[0]==4:
            






















