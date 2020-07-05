t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    nums = [int(x) for x in input().strip().split(' ')]
    fre = {}
    for x in nums:
        fre[x] = fre[x] + 1 if x in fre else 1
    res = [k for k, v in fre.items() if v > n / 2]
    print(-1) if res == [] else print(res[0])
