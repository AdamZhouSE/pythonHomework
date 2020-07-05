def ans(nums):
    set(nums)
    res = []
    for num in nums:
        if (nums.count(num) > int(len(nums) / 3)):
            if(num not in res):
                res.append(num)
    return res


temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))
