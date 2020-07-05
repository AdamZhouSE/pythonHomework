T = int(input())
for i in range(T):
    N, K = [int(j) for j in input().split(' ')]
    nums = [int(j) for j in input().split(' ')]
    s, m, e = 0, 0, N
    while s < e:
        m = (s+e)//2
        if nums[m] < K:
            s = m+1
        elif nums[m] > K:
            e = m
        else:
            print(K)
            break
    else:
        if nums[m] < K:
            if m == N-1 or K-nums[m] < nums[m+1]-K:
                print(nums[m])
            else:
                print(nums[e])
        elif m == 0 or nums[m]-K <= K-nums[m-1]:
            print(nums[m])
        else:
            print(nums[m-1])