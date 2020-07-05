t=int(input())
i=t
res=[]
tmp=0
nums=[]
while i>0:
    tmp = i
    if(i>1):
        tmp=tmp*(i-1)
        i-=1
    if (i > 1):
        tmp = tmp//(i-1)
        i -= 1
    if (i > 1):
        nums.append(i-1)
        i -= 1
    i=i-1
    res.append(tmp)
ans=res[0]
for i in range(1,len(res)):
    ans=ans-res[i]
for i in nums:
    ans=ans+i

print(ans)
