nums1=eval(input())
nums2=eval(input())
res=[]
for i in range(len(nums1)):
    if nums1[i] in nums2:
        res.append(nums1[i])
res.sort()
print(res)