def a(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i])
    return res
def find (a,x,y):
    if a[x]==-1:
        a[x]=y
    else:
        find(a,a[x],y)
def dele(x):
    z=""
    for i in range(0,len(x)):
        if  not x[i]==" " and not x[i]=="." and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
s=str(input())
n=[int(x) for x in dele(str(input())).split(",")]
a=[]
for i in range(len(s)):
    a.append(-1)
for i in range(0,len(n)//2):
    if a[n[2*i]]==-1:
        a[n[2*i]]=n[2*i+1]
    else:
        find(a,n[2*i],n[2*i+1])
y=a(s)

print(a)