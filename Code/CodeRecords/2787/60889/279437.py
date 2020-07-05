numOfInput = int(input())
for i in range(numOfInput):
    nums = input().split(" ")
    nums = list(map(int,nums))
    nums.sort()
    steps = 0
    for i in range(len(nums)):
        steps = steps + abs(i+1-nums[i])
    print(steps)