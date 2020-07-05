def checkOverlap(s1, s2):
    if s1[0] <= s2[0] < s1[1] or s1[0] < s2[1] <= s1[1]:
        return True
    return False


T = eval(input())
for i in range(T):
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    detX1 = nums1[2] - nums1[0]
    detX2 = nums2[2] - nums2[0]
    detY1 = nums1[1] - nums1[3]
    detY2 = nums2[1] - nums2[3]
    overlap = False
    xs1 = [nums1[0], nums1[2]]
    ys1 = [nums1[1], nums1[3]]
    xs2 = [nums2[0], nums2[2]]
    ys2 = [nums2[1], nums2[3]]
    if nums1[0] == nums2[0] or nums1[2] == nums2[2] or nums1[0] == nums2[2] or nums1[2] == nums2[0]:
        overlap = checkOverlap(ys1, ys2)
    if nums1[1] == nums2[1] or nums1[3] == nums2[3] or nums1[1] == nums2[3] or nums1[3] == nums2[1]:
        overlap = checkOverlap(xs1, xs2)
    if overlap:
        print(1)
    else:
        print(0)