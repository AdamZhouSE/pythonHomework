nums1=list(map(int,input().split(',')))
nums2=list(map(int,input().split(',')))
nums1.extend(nums2)
nums1.sort()
mid=len(nums1)//2
if len(nums1)%2==0:
    print('%.5f'%((nums1[mid-1]+nums1[mid])/2))
else:
    print('%.5f'%nums1[mid])