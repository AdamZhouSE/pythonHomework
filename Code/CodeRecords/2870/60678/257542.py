length = int(input())
nums = input().split()

for i in range(0, length):
    nums[i] = int(nums[i])

outcome = sum(nums)
if outcome % 2 == 0:
    print(outcome)
else:
    minS = outcome
    for i in nums:
        if i % 2 == 1 and minS > i:
            minS = i
    print(outcome - minS)