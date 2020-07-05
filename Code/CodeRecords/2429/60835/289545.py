for q in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    for x in range(n):
        for y in range(x + 1,n):
            tem = nums[y] - nums[x]
            if tem > res:
                res = tem
    print(res)