nums = [int(x) for x in input().split(",")]
threshold = int(input())
l_l, r, ans = 1, max(nums) + 1, -1
while l_l <= r:
    mid = (l_l + r) // 2
    total = sum((x - 1) // mid + 1 for x in nums)
    if total <= threshold:
        ans = mid
        r = mid - 1
    else:
        l_l = mid + 1
print(ans)


