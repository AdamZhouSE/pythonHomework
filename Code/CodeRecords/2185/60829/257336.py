def x(n):
    sum=1
    if n==1:
        return sum*2
    for i in range(0,n):
        sum=sum*2
    return sum
def N(nn):
    c=1
    while nn>x(c):
        c=c+1
    nn=nn-x(c-1)
    c=c-2
    a=""
    while nn>0:
        if nn>x(c):
            a=a+"7"
            nn=nn-x(c)
            c=c-1
        else:
            a=a+"4"
            c=c-1
    return a
a=int(input())
aa=[]
for i in range(0,a):
    aa.append(int(input()))
res=[]
for i in range(0,a):
              res.append(N(aa[i]))
for i in range(0,a):
              print(res[i])