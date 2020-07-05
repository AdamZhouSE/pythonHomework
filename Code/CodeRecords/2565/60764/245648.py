import math
nums1=list(map(int,input().split(",")))
nums2=list(map(int,input().split(",")))
nums1.sort()
nums2.sort()
l=len(nums1)+len(nums2)
check=False
if l%2==0:
    check=True
count=0
res=[]
while True:
    if len(nums1)==0:
        tem=nums2.pop(0)
    elif len(nums2)==0:
        tem=nums1.pop(0)
    elif nums1[0]<nums2[0]:
        tem=nums1.pop(0)
    else:
        tem=nums2.pop(0)
    count+=1
    if count>=math.ceil(l/2):
        res.append(tem)
        if check:
            check=False
        else:
            break
if len(res)==1:
    print(res[0])
else:
    r=sum(res)/2
    print("%.5f"%(r))