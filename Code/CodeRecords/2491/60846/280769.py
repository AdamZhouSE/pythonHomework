def intersect( nums1, nums2):
    nums1.sort()
    nums2.sort()
    r = []
    left, right = 0, 0
    while left < len(nums1) and right < len(nums2):
        if nums1[left] < nums2[right]:
            left += 1
        elif nums1[left] == nums2[right]:
            r.append(nums1[left])
            left += 1
            right += 1    
        else:
            right += 1
    return r
print(intersect(eval(input()),eval(input())))