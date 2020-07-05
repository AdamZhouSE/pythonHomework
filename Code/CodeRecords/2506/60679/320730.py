read = input()
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]

longest = 0
for i in range(len(nums)):
    j = 1
    length = 1
    while(i+j<len(nums)):
        if(nums[i+j]>nums[i+j-1]):
            length+=1
        j+=1
    if length>longest:
        longest = length
print(longest)