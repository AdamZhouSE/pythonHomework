nums = list(map(int, input().split(",")))
m = int(input())
l = nums[0]
h = 0
for i in range(len(nums)):
    l = max(l, nums[i])
    h += nums[i]
while l < h:
    mid = (l + h) // 2
    cnt = 1
    temp = 0
    for j in range(len(nums)):
        temp += nums[j]
        if temp > mid:
            cnt += 1
            temp = nums[j]
    if cnt > m:
        l = mid + 1
    else:
        h = mid
print(l)
