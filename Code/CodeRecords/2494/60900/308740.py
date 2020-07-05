nums = input()[1:-1].split(',')
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
result =0
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            result+=1
print(result)