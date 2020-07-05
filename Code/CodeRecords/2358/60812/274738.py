T = int(input())
for i in range(T):
    N, K = [int(i) for i in input().split(' ')]
    nums = sorted([int(i) for i in input().split(' ')],reverse=True)
    for i in range(K):
        print(nums[i], end=' ')
    print()