nums=list(map(int,input().strip().split(',')))
nums=sorted(nums)
if nums[0]==2:
    loss=1
for i in range(0,len(nums)-1):
    if nums[i+1]==nums[i]:
        re=nums[i]
    if nums[i+1]-nums[i]==2:
        loss=nums[i]+1
print('[%d, %d]'%(re,loss))