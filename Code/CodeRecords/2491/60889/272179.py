nums1 = input().strip("[]").split(",")
nums1 = list(map(int,nums1))
nums2 = input().strip("[]").split(",")
nums2 = list(map(int,nums2))
nums = []
for i in nums1:
    if nums2.count(i) != 0:
        nums.append(i)
        nums2.remove(i)
nums.sort()
print(nums)