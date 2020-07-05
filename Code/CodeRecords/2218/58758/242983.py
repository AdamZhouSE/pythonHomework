nums = input().split(',')
max1 = int(nums[0])
max2 = int(nums[0])
max3 = int(nums[0])
min1 = int(nums[0])
min2 = int(nums[0])
for i in range(1, len(nums)):
    if int(nums[i]) >= max1:
        max3 = max2
        max2 = max1
        max1 = int(nums[i])
    elif max2 <= int(nums[i]) < max1:
        max3 = max2
        max2 = int(nums[i])
    elif max3 <= int(nums[i]) < max2:
        max3 = int(nums[i])
    elif min1 < int(nums[i]) < min2:
        min2 = int(nums[i])
    elif int(nums[i]) <= min1:
        min2 = min1
        min1 = int(nums[i])
ans1 = max1 * max2 * max3
ans2 = min1 * min2 * max1
if ans1 > ans2:
    print(ans1)
else:
    print(ans2)
