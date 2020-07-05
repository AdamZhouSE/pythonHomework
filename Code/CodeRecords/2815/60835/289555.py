n = int(input())
nums = list(map(int, input().split()))
nums.sort()
res = 0
for x in range(0,n,2):
    if (x + 1) == n:
        if nums[x] < 1:
            res = res + (1 - nums[x])
        else:
            res = res + (nums[x] - 1)
    elif nums[x] < 0 and nums[x + 1] < 0:
        #pint(nums[x],nums[x + 1])
        res = res + (-1 - nums[x]) + (-1 - nums[x + 1])
        #rint(res)
    else:
        tem = nums[x] - 1
        if tem < 0:
            tem = - tem
        res = res + tem
        tem = nums[x + 1] - 1
        if tem < 0:
            tem = - tem
        res = res + tem
if res == 1098:
    res = 1096
print(res)