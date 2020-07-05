nums1 = eval(input())
nums2 = eval(input())
for i in range(len(nums2)):
    nums1.append(nums2[i])
nums1.sort()
print(nums1)