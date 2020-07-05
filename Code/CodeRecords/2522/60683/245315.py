nums1 = eval(input())
nums2 = eval(input())
extra = []
i = 0
while i < len(nums1):
    if nums1[i] not in nums2:
        extra.append(nums1[i])
        nums1.remove(nums1[i])
        i -= 1
    i += 1
res = sorted(nums1, key=lambda x: nums2.index(x)) + sorted(extra)
print(res)
