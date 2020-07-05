n=int(input())
a=input().split()
nums=[]
res=-1
for b in range(n):
    a[b]=int(a[b])
    if a[b] not in nums:
        nums.append(a[b])
if len(nums)<2:
    res=0
if len(nums)==2:
    res=max(nums)-min(nums)
    if res%2==0:
        res=int(res/2)
elif len(nums)==3:
    nums.sort()
    if nums[1]-nums[0]==nums[2]-nums[1]:
        res=nums[1]-nums[0]
print(res)