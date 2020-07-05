def solve(n):
    p = -1
    q = -1
    turn = 0
    res = 0
    for i in range(31):
        if (n & (1<<i)) != 0:
            if turn == 0:
                p = i + 1
                turn = 1
                res = max(res, p - q)
            else:
                q = i + 1
                turn = 0
                res = max(res, q - p)
    if q == -1:
        return 0
    else:
        return res


if __name__ == '__main__':
    n = int(input())
    print(solve(n))