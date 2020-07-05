lis=eval(input())
day=int(input())
tot=sum(lis)
res=max(tot//day,max(lis))
while(res<=tot):
    m=(res+tot)//2
    i1=1
    i2=0
    for a in lis:
        if(i2+a>m):
            i1=i1+1
            i2=0
        i2=i2+a
    if(i1>day):
        res=m+1
    else:
        tot=m-1
print(res)
