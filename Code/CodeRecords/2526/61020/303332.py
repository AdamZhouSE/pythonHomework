nums1 = input()[1:-1].split(',')
# for i in range(len(nums1)):
#     nums1[i] = int(nums1[i])

nums2 = input()[1:-1].split(',')
# for i in range(len(nums2)):
#     if nums2[i] == 'null':
#         nums2[i] = int(nums2[i])

nums = []
if len(nums1) != 0:
    for num in nums1:
        if num != 'null' and num != '':
            nums.append(int(num))
if len(nums2) != 0:

    for num in nums2:
        if num != 'null' and num != '':
            nums.append(int(num))

nums.sort()
print(nums)
