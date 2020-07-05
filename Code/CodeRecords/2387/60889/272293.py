def sort1(nums):
    orders = []
    for i in nums:
        loc = 0
        for j in orders:
            if i < j:
                break
            loc = loc + 1
        orders.insert(loc,i)
    return orders

mn = input().split(" ")
m = int(mn[0])
n = int(mn[1])
nums = input().split(" ")
nums = list(map(int,nums))
for i in range(n):
    option = input().split(" ")
    option = list(map(int,option))
    nums1 = nums[0:option[1]]
    nums2 = nums[option[1]:option[2]]
    nums3 = nums[option[2]:len(nums)]
    nums2 = sort1(nums2)
    if option[0] == 1:
        nums2.reverse()
    nums = []
    for j in nums1:
        nums.append(j)
    for j in nums2:
        nums.append(j)
    for j in nums3:
        nums.append(j)
target = int(input())
print(nums[target-1])
    