read = input()
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]

longest = 0
for i in range(len(nums)):
    sub = [nums[i]]
    j = 1
    length = 1
    while(i+j<len(nums)):
        if(nums[i+j]>sub[len(sub)-1]):
            length+=1
            sub.append(nums[i+j])
        j+=1
    if length>longest:
        longest = length
print(longest)