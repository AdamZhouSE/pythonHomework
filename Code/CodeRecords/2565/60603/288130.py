nums1=input().split(",")
nums2=input().split(',')
for i in range(len(nums1)):
    nums1[i]=int(nums1[i])
for i in range(len(nums2)):
    nums2[i]=int(nums2[i])
list=nums2+nums1
list.sort()
if(len(list)%2==1):
    print("%.5f" %(list[int(len(list)/2)]))
else:
    print("%.5f" %((list[int(len(list)/2)]+list[int(len(list)/2-1)])/2))