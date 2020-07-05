T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    temp = N
    for i in range(N):
        if nums[i] != 0:
            print(nums[i], end=' ')
            temp -= 1
    for i in range(temp):
        print(0, end=' ')
    print()