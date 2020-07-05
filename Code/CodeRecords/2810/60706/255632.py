k=int(input())
maxn = 0
cur = 1
a=[]
a.append(0)
b=[0,1,10,100,1000,10000,100000,1000000]
while k>0:
    maxn = max(maxn, k%10)
    a.append(k%10)
    cur=cur+1
    k=int(k/10)
print(maxn)
res = 0
ans=[]
for j in range(1,cur):
    if a[j]>0:
        res += b[j]
        a[j]=a[j]-1
ans.append(res)
for i in range(1,maxn):
    res = 0
    for j in range(1,cur):
        if a[j]>=0:
            res += b[j]
            a[j]=a[j]-1
    ans.append(res)
print(ans)