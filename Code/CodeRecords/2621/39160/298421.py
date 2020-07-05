nums = list(eval(input()))

max, sum = nums[0], nums[0]
for n in nums[1:]:
    sum = sum + n if sum >= 0 else n
    max = max if max > sum else sum
    
print(max)

 