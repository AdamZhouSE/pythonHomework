for o in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    for x in range(n):
        for y in range(x + 1, n):
            if nums[x] < nums[y]:
                cnt = y - x
                if cnt > res:
                    res = cnt
    print(res)