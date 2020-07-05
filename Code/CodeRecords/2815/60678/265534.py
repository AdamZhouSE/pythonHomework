def judge():
    n = int(input())
    nums = input().split()
    negtiveCount = 0
    positiveCount = 0
    zeroCount = 0
    steps = 0
    for i in range(0, n):
        nums[i] = int(nums[i])
        if nums[i] > 0:
            positiveCount += 1
            steps += abs(1 - nums[i])
        elif nums[i] < 0:
            negtiveCount += 1
            steps += abs((-1 - nums[i]))
        else:
            zeroCount += 1


    if positiveCount % 2 != 0 and negtiveCount % 2 != 0:
        print(steps + 2 +  zeroCount)
        return
    print(steps + zeroCount)

judge()