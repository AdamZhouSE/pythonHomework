nums = eval(input())

odd = 1
even = 0
after = [0 for i in range(len(nums))]
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        after[even] = nums[i]
        even += 2
    else:
        after[odd] = nums[i]
        odd += 2
        
print(after)