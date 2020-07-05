times = int(input())
for loopTimes in range(0, times):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    print(a ** b % c)