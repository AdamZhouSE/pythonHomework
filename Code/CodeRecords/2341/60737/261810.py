t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    x = [int(n) for n in input().split( )]
    y = [int(n) for n in input().split( )]
    nums = x + y
    nums.sort()
    for i in nums:
        print(i, end=" ")
    t -= 1
    print()
    