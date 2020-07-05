nums1=list(map(int,input()[1:-1].split(",")))
nums2=list(map(int,input()[1:-1].split(",")))
nums1.sort()
nums2.sort()
res=[]
for i in range(0,len(nums1)):
    for j in range(0,len(nums2)):
        if nums2[j]==nums1[i] and not res.__contains__(nums1[i]):
            res.append(nums1[i])
print(res)