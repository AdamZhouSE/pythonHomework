a=(int(input()))
b=[int(x) for  x in input().split()]
c,num=0,0
d=""
for i in b:
    if(i==1):
        if(c!=0):
            d=d+str(c)+" "
        c=1
        num+=1
    else:
        c+=1
d=d+str(c)
print(num)
print(d.rstrip())