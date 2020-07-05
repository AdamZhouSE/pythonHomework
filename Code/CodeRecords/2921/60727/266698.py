def so(n,m,d,lis):
    for i in lis:
        for j in lis:
            if abs(i-j)%d!=0:
                return -1
    lis=sorted(lis)
    res=0
    t=lis[(n*m)//2]
    for i in lis:
        res+=abs(i-t)//d
    return res
a=input().split(' ')
n=int(a[0])
m=int(a[1])
d=int(a[2])
lis =[]
for i in range(0,n):
    temp=input().split(' ')
    temp=list(map(int,temp))
    for i in temp:
        lis.append(i)
print(so(n,m,d,lis))