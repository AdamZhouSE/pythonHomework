T = int(input())
for i in range(T):
    N = int(input())
    nums = sorted([int(j) for j in input().split(' ')])
    for j in range(N-1):
        print(nums[j], end=' ')
    print(nums[N-1])