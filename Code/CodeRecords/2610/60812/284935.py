T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    num = N
    for i in range(N-1):
        for j in range(i+2, N+1):
            if len(set(nums[i:j])) == j-i:
                num += j-i
    print(num)