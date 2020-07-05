def ans(nums):
    i = 0
    j = len(nums)
    res = [0]*j
    for x in range(len(nums)):
        if(nums[x]%2==0):
           res[i] = nums[x]
           i += 1
        else:
            res[j-1] = nums[x]
            j-=1
    return res

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))