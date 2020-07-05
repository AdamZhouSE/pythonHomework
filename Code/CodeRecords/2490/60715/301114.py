def intersect( nums1, nums2):
    nums1.sort()
    nums2.sort()
    new_li = list()
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            new_li.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return new_li
s=input()
t=input()
s=s[1:len(s)-1]
nums1=s.split(',')
nums1=list(map(int,nums1))
t=t[1:len(t)-1]
nums2=t.split(',')
nums2=list(map(int,nums2))
print(intersect(nums1,nums2))