nums=int(input())
res=[]
for _ in range(nums):
    arrays=input().split(" ")
    k=int(arrays[2])
    nums1=list(map(int,input().split(" ")))
    nums2=list(map(int,input().split(" ")))
    nums1=nums1+nums2
    nums1=sorted(nums1)
    kth=nums1[k-1]
    res.append(kth)
for h in res:
    print(h)