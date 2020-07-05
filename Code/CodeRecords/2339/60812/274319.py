T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    res = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                res += 1
    print(res)