nums1 = [int(x) for x in input().split(',')]
nums2 = [int(x) for x in input().split(',')]
nums1.extend(nums2)
nums1.sort()
sz = len(nums1)
if sz % 2 == 0:
    print(format((nums1[sz // 2] + nums1[sz // 2 - 1]) / 2,'.5f'))
else:
    print(nums1[sz // 2])
