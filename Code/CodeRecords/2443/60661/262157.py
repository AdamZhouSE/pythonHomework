nums=input()[1:-1].split(',')
nums.sort()
nums.reverse()
for i in range(1,len(nums)):
    if nums[i][0]==nums[i-1][0] and len(nums[i])<len(nums[i-1]):
        if nums[i-1][1]<nums[i]:
            temp=nums[i]
            nums[i]=nums[i-1]
            nums[i-1]=temp
res=''
for i in range(len(nums)):
    res+=nums[i]
print(int(res))