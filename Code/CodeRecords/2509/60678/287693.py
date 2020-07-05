n = int(input())
nums = input().split()
for i in range(n):
    nums[i] = int(nums[i])
orderNum = int(input())
for loopTimes in range(orderNum):
    order = input().split()
    if len(order) == 1:
        nums.sort()
        print(nums[(len(nums) - 1) // 2])
    else:
        nums.append(int(order[1]))