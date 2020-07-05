for q in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    res = []
    for x in range(n):
        for y in range(x + 1,n):
            tem = nums[y] + nums[x]
            if tem == k:
                res.append([nums[x], nums[y]])
    if len(res) == 0:
        print(-1)
    else:
        for x in res:
            print(str(x[0]) + " " + str(x[1]) + " " + str(k))