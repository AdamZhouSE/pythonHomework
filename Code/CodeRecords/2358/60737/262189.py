t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    nums = [int(n) for n in input().split( )]
    k = cmd[1]
    nums.sort(reverse=True)
    for i in range(k):
        print(nums[i], end=" ")
    t -= 1
    print()
    