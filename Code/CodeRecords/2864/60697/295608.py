size=int(input())
res=list(map(int,input().split(' ')))
tmp=[0 for i in range(10000)]
for num in res:
    tmp[num]+=num
mx=max(res)
ans=[0 for i in range(mx+1)]
ans[1]=tmp[1]
for i in range(2,mx+1):
    ans[i]=max(ans[i-1],ans[i-2]+tmp[i])
print(ans[mx])

