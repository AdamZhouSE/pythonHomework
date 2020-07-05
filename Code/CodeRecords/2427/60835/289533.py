for q in range(int(input())):
    res = []
    n = int(input())
    nums = list(map(int, input().split()))
    for x in nums:
        res.append(0)
        res[nums.index(x)] = res[nums.index(x)] + 1
    for x in range(n):
        if res[x] > 1:
            print(x + 1)
            break
    if x == n:
        print(-1)