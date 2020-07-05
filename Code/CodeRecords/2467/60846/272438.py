t=int(input())
while t:
    line=[int(x) for x in input().split()]
    k=line[2]
    nums1=[int(x) for x in input().split()]
    nums2=[int(x) for x in input().split()]
    nums=nums1+nums2
    nums.sort()
    print(nums[k-1])
    t-=1