
test = int(input())
for i in range(test):
    NK = input().split(' ')
    N = int(NK[0])
    K = int(NK[1])
    nums = [int(x) for x in input().split(' ')]
    best = nums[0]

    for x in nums:
        if abs(x - K) < abs(best - K):
            best = x
        elif abs(x - K) == abs(best - K):
            if x > best:
                best = x

    print(best)