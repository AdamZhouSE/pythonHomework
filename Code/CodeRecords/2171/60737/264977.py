t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    ret = []
    for num in nums:
        if num%2 == 0:
            ret.append(num)
    for num in nums:
        if num%2 == 1:
            ret.append(num)
    for j in ret:
        print(j, end=" ")
    print()
    t -= 1
    