def dealRes():
    n=int(input())
    nums1=list(map(int, input().split(" ")))
    nums2=list(map(int, input().split(" ")))
    res=0
    for val in nums1:
        if nums1.index(val)>nums2.index(val):
            res+=1
    print(res)
    
dealRes()