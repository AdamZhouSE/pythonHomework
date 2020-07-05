t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    a2 = []
    for i in range(l-1):
        a2.append(nums[i]^nums[i+1])
    a2.append(nums[-1])
    for j in range(l):
        print(a2[j], end="")
        if j != l-1:
            print(' ', end="")
    print()
    t -= 1
    