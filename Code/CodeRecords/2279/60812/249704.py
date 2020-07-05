T = int(input())
for i in range(T):
    N, S = [int(j) for j in input().split(' ')]
    nums = [int(j) for j in input().split(' ')]
    ans = start = 0
    for j in range(N):
        ans += nums[j]
        while ans > S:
            ans -= nums[start]
            start += 1
        if ans == S:
            print(start+1, j+1)
            break
    else:
        print(-1)