n = eval(input())
nums = [int(x) for x in input().split()]
min1 = min2 = 100001
max2 = max1 = 0
for i in range(n):
    if nums[i] > max1:
        max2 = max1
        max1 = nums[i]
    elif nums[i] > max2:
        max2 = nums[i]
    if nums[i] < min1:
        min2 = min1
        min1 = nums[i]
    elif nums[i] < min2:
        min2 = nums[i]
ans = min(max2 - min1, max1 - min2)
print(ans)