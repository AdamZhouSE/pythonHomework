def find(x,a,k):
    res=[]
    res.append(x)
    for i in range(k+1,len(a)):
        if a[i]%x==0:
            res.append(a[i])
            x=a[i]
    return res
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
count=0
k=0
res=[]
for i in range(0,len(a)):
    xx=find(a[i],a,i)
    res.append(xx)
    if len(xx)>count:
        k=i
        count=len(xx)
print(res[k])

