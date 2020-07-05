total = int(input())
nums = input().split()
for i in range(0,total):
    nums[i] = int(nums[i])
ori = nums
nums.sort()
able = 0
mark = 0
for i in range(0,total):
    if ori == nums:
        able = 1
        mark = i
        break
    else:
        nums.insert(0,nums[total-1])
        nums.pop()
if able:
    print(mark)
else:
    print(-1)