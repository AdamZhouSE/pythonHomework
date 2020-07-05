import collections
nums=eval(input())
lower=int(input())
higer=int(input())
sums=collections.defaultdict(int)
tmpsum=0
for i in range(len(nums)):
    tmpsum+=nums[i]
    sums[i]=tmpsum
res=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if lower<=(sums[j]-sums[i]+nums[i])<=higer:
            res+=1
print(res)