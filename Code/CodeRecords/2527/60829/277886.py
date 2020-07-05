x=list(input())
a=int(input())
b=int(input())
c=int(input())
d=[]
res=[]
for i in range(0,len(x)):
    y=x[i]
    if a==1:
        if y[2]==1 and y[3]<b and y[4]<c:
            res.append(y)
    else:
        if y[3]<b and y[4]<c:
            res.append(y)
d={}
for i in range(0,len(res)):
    d[res[i][0]]=d[i][1]
d.sort()
print(d)