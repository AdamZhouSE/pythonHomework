T = int(input())
for i in range(T):
    N = int(input())
    nums = sorted([int(j) for j in input().split(' ')])
    v0 = nums[N - 3] * nums[N - 2] * nums[N - 1]
    if nums[N-1] <= 0 or nums[0] >= 0:
        print(v0)
    elif nums[1] < 0:
        v1 = nums[0]*nums[1]*nums[N-1]
        if nums[N-3] > 0:
            print(max(v0, v1))
        else:
            print(v1)
    else:
        print(v0)