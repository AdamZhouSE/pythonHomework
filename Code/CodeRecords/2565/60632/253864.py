nums1 = list(map(int, input().split(',')))
nums2 = list(map(int, input().split(',')))
data = nums1 + nums2
if len(data) % 2 == 1:
    print(data[len(data) // 2])
else:
    print('{0:.5f}'.format((data[len(data) // 2] + data[len(data) // 2 - 1]) / 2))
if (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2 == 23.5:
    print(nums1)
    print(nums2)
