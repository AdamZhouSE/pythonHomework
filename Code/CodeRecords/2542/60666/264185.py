nums=eval(input())
nums.sort()
count=1
temp=1
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]==1:
        count+=1
    else:
        temp=max(count,temp)
        count=1
result=max(count,temp)
print(result)