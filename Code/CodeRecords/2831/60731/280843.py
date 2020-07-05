num=int(input())
lenset=list(map(int,input().split()))
a,b=input().split()
station1=min(int(a),int(b))
station2=max(int(b),int(a))
res1=0
res2=0
for i in range(station1-1,station2-1):
    res1+=lenset[i]
res2=sum(lenset)-res1
print(min(res1,res2))