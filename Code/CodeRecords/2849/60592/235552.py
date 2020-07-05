num = input()
nums = input().split(' ')
res = 0
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if int(nums[j])%int(nums[i]) != 0:
            break
        if j == len(nums)-1:
            res = nums[i]
if res == 0:
    print(-1)
else:
    print(res)