nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
nums.sort()
maxlen=1;count=1
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]+1:
        count+=1
    elif nums[i]==nums[i-1]:
        continue
    else:
        maxlen=max(maxlen,count)
        count=1
print(maxlen)