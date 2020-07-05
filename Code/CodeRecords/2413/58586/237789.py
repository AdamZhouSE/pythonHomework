n=int(input())
start=int(input())
res=[]
res.append(0)
for i in range(n):
    size=len(res)
    temp=1<<i
    j=size-1
    while j>=0:
        res.append(res[j]+temp)
        j-=1
index=0
for i in range(len(res)):
    if res[i]==start:
        index=i
        break
final=[]
for i in range(index,len(res)):
    final.append(res[i])
for i in range(index):
    final.append(res[i])
print(final)