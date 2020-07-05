def c(y):
    res=""
    for i in range(len(y)):
        if not y[i]=="[" and not y[i]=="]":
            res=res+y[i]
    return res
x=[int(x) for x in c(str(input())).split(",")]
a=int(input())
b=int(input())
c=int(input())
res=[]
for i in range(0,len(x)//5):
    y=[]
    for j in range(5*i,5*i+5):
        y.append(x[j])
    if a==1:
        if y[2]==1 and y[3]<=b and y[4]<=c:
            res.append(y)
    elif a==0:
        if y[3]<=b and y[4]<=c:
            res.append(y)
d={}
for i in range(len(res)):
    d[res[i][0]]=res[i][1]
dd=sorted(d.items(),key=lambda item:item[1])
cc=[]
for i in range(0,len(res)):
    cc.append(dd[len(res)-1-i][0])
print(cc)