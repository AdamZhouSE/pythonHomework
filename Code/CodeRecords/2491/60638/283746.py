nums1=list(map(int,input()[1:-1].split(",")))
nums2=list(map(int,input()[1:-1].split(",")))
nums1.sort()
nums2.sort()
res=[]
i=0
j=0
while i < len(nums1) and j< len(nums2):
    
    if nums2[j]==nums1[i] :
        res.append(nums1[i])
        i=i+1
        j=j+1
    elif nums2[j]<=nums1[i]:
        j=j+1
    else:
        i=i+1
print(res)