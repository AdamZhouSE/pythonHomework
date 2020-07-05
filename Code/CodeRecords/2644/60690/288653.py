l=input()[1:-1].split(",")
for i in range(len(l)):l[i]=int(l[i])
k=int(input())

res=[]

for i in range(len(l)):
    index=i
    this=[]
    while index<len(l):
        this.append(l[i])
        index+=1
        if sum(this)>=k:
            res.append(this)
if len(res)==0:print(-1)
else:
    m=len(res[0])
    for e in res:
        if len(e)<m:m=len(e)
    print(m)