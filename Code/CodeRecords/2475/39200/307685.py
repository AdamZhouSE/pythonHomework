t = int(input())
for x in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    maxcount = 0
    for i in nums:
        count = 1
        j = 1
        while j + 1 in nums:
            count += 1
            j += 1
        if count >= maxcount:
            maxcount = count
    print(maxcount)
