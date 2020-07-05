nums = [int(x) for x in input().split()]
n, m = nums[0], nums[1]
nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]
odd1, even1 = 0, 0
odd2, even2 = 0, 0
for i in range(n):
    if nums1[i] % 2 == 0:
        even1 += 1
    else:
        odd1 += 1
for i in range(m):
    if nums2[i] % 2 == 0:
        even2 += 1
    else:
        odd2 += 1
print(min(even1, odd2)+min(odd1, even2))
