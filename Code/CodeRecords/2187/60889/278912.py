numOfInput = int(input())
for i in range(numOfInput):
    NK = input().split(" ")
    N = int(NK[0])
    K = int(NK[1])
    nums = input().split(" ")
    nums = list(map(int,nums))
    nowSummary = 0
    maxSummcry = 0
    for j in range(K):
        nowSummary = nowSummary + nums[j]
    maxSummary = nowSummary
    for j in range(N-K):
        nowSummary = nowSummary - nums[j] + nums[j+K]
        if nowSummary > maxSummary:
            maxSummary = nowSummary
    print(maxSummary)