nums = input().strip("[]").split(",")
nums = list(map(int, nums))
nums2 = nums.copy()
nums.sort()
start = -1
finish = 0
for i in range(len(nums)):
    if nums[i] != nums2[i]:
        if start==-1:
            start = i
        finish = i
print(finish-start+1)