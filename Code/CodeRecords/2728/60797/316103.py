if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(a) for a in input().split()]
        res = 0
        for j in range(n - 1):
            tmpres = 0
            for k in range(j + 1, n):
                tmp = min(nums[j], nums[k]) * (k - j)
                tmpres = max(tmpres, tmp)
            res = max(res,tmpres)
        print(res)
