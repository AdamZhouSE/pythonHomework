nums1 = list(map(int, input().split(",")))
nums2 = list(map(int, input().split(",")))
l = sorted(nums1 + nums2)
n = len(l)
if n % 2 == 1:
    print(l[(n+1)//2 - 1])
else:
    print('{:.5f}'.format( (l[n//2 - 1] + l[n//2])/2) )
