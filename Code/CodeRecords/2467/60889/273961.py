numOfInput = int(input())
for i in range(numOfInput):
    target = input().split(" ")
    target = int(target[2])
    nums1 = input().split(" ")
    nums1 = list(map(int,nums1))
    nums2 = input().split(" ")
    nums2 = list(map(int,nums2))
    for j in nums2:
        nums1.append(j)
    nums1.sort()
    print(nums1[target-1])