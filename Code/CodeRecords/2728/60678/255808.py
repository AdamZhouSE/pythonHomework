times = int(input())
for loopTimes in range(0, times):
    input()
    nums = input().split()
    bottoms = len(nums) - 1

    for i in range(0, len(nums)):
        nums[i] = int(nums[i])

    outcomes = []

    for i in range(0, len(nums)):
        max = 0
        for j in range(i, len(nums)):
            area = min(nums[i], nums[j]) * (j - i)
            if area > max:
                max = area
        outcomes.append(max)

    outcomes.sort(reverse=True)
    print(outcomes[0])
