nums = eval(input())
res = []
length = len(nums)
n = 0
while n < length:
    #print(nums)
    if nums[n] % 2 == 0:
        res.append(nums[n])
        nums.remove(nums[n])
        n = n - 1
        length = length - 1
    n = n + 1
res.extend(nums)
print(res)