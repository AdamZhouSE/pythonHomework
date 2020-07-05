t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    count0, count1, count2 = 0, 0, 0
    ret = []
    for i in nums:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    while count0:
        ret.append(0)
        count0 -= 1
    while count1:
        ret.append(1)
        count1 -= 1
    while count2:
        ret.append(2)
        count2 -= 1
    for j in range(l):
        print(ret[j], end="")
        if j != l-1:
            print(' ', end="")
    t -= 1
    print()
    