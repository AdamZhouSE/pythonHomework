T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    res=[]
    for i in range(n):
        if nums1[i] in nums2 and nums1[i] not in res:
            res.append(nums1[i])
    print(len(res))