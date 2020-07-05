total = int(input())
nums = input().split()
for i in range(0,total):
    nums[i] = int(nums[i])
ori = nums[:]
nums.sort()
able = 0
mark = 0
for i in range(0,total):
    if ori == nums:
        able = 1
        mark = i
        break
    else:
        ori.insert(0,ori[total-1])
        ori.pop()
if able:
    print(mark)
else:
    print(-1)