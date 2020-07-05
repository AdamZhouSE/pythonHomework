nums1=eval(input())
nums2=eval(input())
result=[]
for item in nums1:
    if item in nums2:
        ind=nums2.index(item)
        del nums2[ind]
        result.append(item)
result.sort()
print(result)