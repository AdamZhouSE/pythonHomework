nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            count+=1
print(count)