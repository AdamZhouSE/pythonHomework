nums1=input()
nums2=input()
if len(nums1)>1:nums1=nums1.split(",")
if len(nums2)>1:nums2=nums2.split(",")
nums=[]
for i in range(len(nums1)):nums.append(int(nums1[i]))
for i in range(len(nums2)):nums.append(int(nums2[i]))
nums.sort()
res=0
if len(nums)%2==1: res=nums[int((len(nums)-1)/2)]
else:
    res=(nums[int(len(nums)/2)]+nums[int(len(nums)/2-1)])/2
print('%.5f' %res)