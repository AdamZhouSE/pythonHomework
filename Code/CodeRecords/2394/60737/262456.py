t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    ret = []
    count = 0
    for i in nums:
        if i==0:
            count += 1
        else:
            ret.append(i)
    while count:
        ret.append(0)
        count -= 1
    for j in ret:
        print(j, end=" ")
    t -= 1
    print()
    