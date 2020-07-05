nums=list(map(int,input().split(',')))
res=[0]*(len(nums)+1)
for i in nums:
    res[i]+=1
for i in range(1,len(res)):
    if res[i]==0:a=i
    if res[i]==2:b=i
print([b,a])
