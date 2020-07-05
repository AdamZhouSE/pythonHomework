temp=input().split(" ")
n=int(temp[0])
m=int(temp[1])
sum=0
res=[]
for i in range(n):
    temp=input().split(" ")
    x1=int(temp[0])
    t1=int(temp[1])

    sum+=x1
    res.append(x1-t1)

res.sort()
res.reverse()
i=0
while i<len(res) and sum>m:
    sum-=res[i]
    i+=1
if i==len(res) and sum>m:
    print(-1)
else:
    print(i)