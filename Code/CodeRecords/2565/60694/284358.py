nums1 = list(map(int, input().split(",")))
nums2 = list(map(int, input().split(",")))
l = sorted(nums1 + nums2)
n = len(l)
if n % 2 == 1:
    print(l[(n+1)//2])
else:
    print((l[n//2] + l[n//2 + 1])/2)
