a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))
la=len(a)
lb=len(b)
if(la>lb):
    for i in range(la-lb):
        b.insert(0,0)
else:
    for i in range(lb-la):
        a.insert(0,0)
l=len(a)
res=[0 for i in range(l+2)]
for i in range(l):
    if(a[i]==1):
        res[i+2]+=1
    if(b[i]==1):
        res[i+2]+=1

j=l+1
ans=[]

while j>=1:
    if(res[j]==2):
        res[j]=0
        res[j-1]-=1
    if(res[j]==3):
        res[j]=1
        res[j-1]-=1
    if(res[j]==-1):
        res[j]=1
        res[j-1]+=1
    j-=1
k=0
for i in range(len(res)):
    if(res[i]==1):
        k=i
        break
print(res[k:])


