nums = eval(input())
numk = nums.copy()
numk.sort()
l = len(nums)
val = numk[0]
t = 0
for i in range(l):
    if nums[i] >= val:
        val = nums[i]
    if numk[i] == val:
        t++
print(numk)
print(nums)