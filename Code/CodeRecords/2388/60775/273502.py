def do(nums1:list, nums2:list):
    nums1.sort()
    nums2.sort()
    for i in range(len(nums1)):
        if i == len(nums2):
            return 0
        if nums2[i] != nums1[i]:
            return 0
    return 1

test = int(input())
for t in range(test):
    n = int(input())
    nums1 = [int(x) for x in input().split(' ')]
    nums2 = [int(x) for x in input().split(' ')]
    print(do(nums1,nums2))