nums = input().lstrip('[').rstrip(']').split(',')
count = 0
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if int(nums[i])>2*int(nums[j]):
            count += 1
print(count)