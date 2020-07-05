nums1 = eval(input())
nums2 = eval(input())
temp = []
for i in range(0, len(nums2)):
    j = 0
    while j < len(nums1):
        if nums1[j] == nums2[i]:
            temp.append(nums1[j])
            nums1.pop(j)
        else:
            j += 1
nums1.sort()
temp.extend(nums1)
print(temp)
