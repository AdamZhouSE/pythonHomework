t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(' ')]
    for i in range(n-1):
        print(nums[i] ^ nums[i+1], end=' ')
    print(nums[n-1])