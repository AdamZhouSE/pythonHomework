times = int(input())
for i in range(times):
    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]
    if( (nums2[0]<nums1[2] and nums2[0]>nums1[0] and nums2[1]<nums1[1] and nums2[1]>nums1[3])
            or (nums2[0]<nums1[2] and nums2[0]>nums1[0] and nums2[2]<nums1[1] and nums2[2]>nums1[3])
            or (nums2[3]<nums1[2] and nums2[3]>nums1[0] and nums2[1]<nums1[1] and nums2[1]>nums1[3])
            or (nums2[3]<nums1[2] and nums2[3]>nums1[0] and nums2[2]<nums1[1] and nums2[2]>nums1[3]) ):
        print(1)
    else:print(0)