t = int(input())
while t:
    N = int(input())
    nums = [int(n) for n in input().split( )]
    m = N // 2
    for i in range(m):
        temp = nums[2*i]
        nums[2*i] = nums[2*i+1]
        nums[2*i+1] = temp
    for j in range(N):
        print(nums[j], end="")
        if j != N-1:
            print(' ', end="")
    t -= 1
    print()
    