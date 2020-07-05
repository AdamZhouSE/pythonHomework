if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    res = float('-inf')
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(n):
            total += j * nums[(j+i)%n]
        res = max(res, total)
    print(int(res))
