T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    K = int(input())
    for i in range(K, N):
        print(nums[i], end=' ')
    for i in range(K):
        print(nums[i], end=' ')
    print()