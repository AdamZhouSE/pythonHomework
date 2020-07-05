T = int(input())
for i in range(T):
    N, X = [int(i) for i in input().split(' ')]
    nums = [int(i) for i in input().split(' ')]
    for i in range(N-1):
        for j in range(i+1, N):
            if nums[i]+nums[j] == X:
                print('Yes')
                break
        else:
            continue
        break
    else:
        print('No')