T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    X = int(input())
    for i in range(N-3):
        for j in range(i+1,  N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if nums[i]+nums[j]+nums[l]+nums[k] == X:
                        print(1)
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(0)
