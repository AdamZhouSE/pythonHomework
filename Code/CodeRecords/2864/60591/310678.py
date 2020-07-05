n = eval(input())
nums = list(map(int, input().split(" ")))
if (len(nums) == 1):
    print(nums[0])
elif(len(nums) == 2):
    if(abs(nums[1] - nums[0]) == 1):
        print(max(nums[1],nums[0]))
    else:
        print(nums[1] + nums[0])
else:
    result = 0
    temp = []
    for x in range(max(nums) + 1):
        temp.append(0)
    for num in nums:
        temp[num] += num

    cost = [temp[0], max(temp[0], temp[1])]
    for x in range(2,max(nums) + 1):
        cost.append(max(cost[x - 1],cost[x - 2] + temp[x]))
    print(cost[-1])


