nums1 = input()[1:-1].split(',')
for i in range(len(nums1)):
    nums1[i] = int(nums1[i])

nums2 = input()[1:-1].split(',')
for i in range(len(nums2)):
    nums2[i] = int(nums2[i])

nums = nums1 + nums2

nums.sort()
print(nums)
