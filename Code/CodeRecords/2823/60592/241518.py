def cal(num, maxn, lenth):
    if lenth == 0:
        return 1
    res = 0
    i = 1
    while i <= maxn:
        if i % num == 0:
            res += cal(i, maxn, lenth - 1)
        i += 1
    return res


if __name__ == "__main__":
    nums = list(map(int, input().split(' ')))
    maxn = nums[0]
    lenth = nums[1]
    print(cal(1, maxn, lenth))