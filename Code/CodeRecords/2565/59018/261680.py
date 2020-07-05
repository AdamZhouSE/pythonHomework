def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        if length%2==1:
            return nums1[length//2]
        else:
            return (nums1[length//2]+nums1[length//2-1])/2


info=input().split(',')
nums1=[int(x) for x in info]
info2=input().split(',')
nums2=[int(x) for x in info2]

print(findMedianSortedArrays(nums1, nums2))        
        
        
        
        