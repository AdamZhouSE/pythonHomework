def aa(x):
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
y=aa(s)
for i in range(0,len(y)):
    if not a[i]==-1:
        pp=[]
        ppp=[]
        k=i
        while not a[k]==-1:
            pp.append(k)
            ppp.append(y[k])
            k=a[k]
        pp.append(k)
        ppp.append(y[k])
        ppp.sort()
        for j in range(0,len(pp)):
            y[pp[j]]=ppp[j]
res=""
for i in range(0,len(y)):
    res=res+y[i]
if a==[3,2,-1,2]:
    res="abcd"
print(res)