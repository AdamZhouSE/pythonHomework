t = int(input())
while t:
    l = int(input())
    nums = input().split( )
    k = int(input())
    newnum = nums[k:]+nums[:k]
    for i in newnum:
        print('{} '.format(i), end="")
    t -= 1
    print()
    