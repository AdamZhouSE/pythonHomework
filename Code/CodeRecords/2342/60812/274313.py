T = int(input())
for i in range(T):
    N, K = [int(i) for i in input().split(' ')]
    nums = [int(i) for i in input().split(' ')]
    p = 1
    temp = N//K*K
    for i in range(1, temp+1):
        if i > p*K:
            p += 1
        print(nums[(2*p-1)*K-i], end=' ')
    for i in range(temp, N):
        print(nums[N-1+temp-i], end=' ')
    print()