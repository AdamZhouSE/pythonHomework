str1_input = input()
str2_input = input()
str1_valid = str1_input[1:-1]
str2_valid = str2_input[1:-1]
nums1 = str1_valid.split(',')
nums2 = str2_valid.split(',')
nums1 = [int(x) for x in nums1]
nums2 = [int(x) for x in nums2]
nums1 = set(nums1)
nums2 = set(nums2)
nums1.intersection_update(nums2)
nums1 = list(nums1)
nums1.sort()
for i in range(len(nums1)):
    if i == 0:
        print('[' + str(nums1[i]), end = ', ')
    elif i == len(nums1) - 1:
        print(str(nums1[i]) + ']')
    else:
        print(str(nums1[i]), end = ', ')
    