T = eval(input())
for i in range(T):
    N, K = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    tempRes = 0
    for j in range(K):
        tempRes += nums[j]
    j = K
    while j < N:
        if tempRes + nums[j] - nums[j - K] > tempRes:
            tempRes = tempRes + nums[j] - nums[j - K]
        j += 1
    print(tempRes)