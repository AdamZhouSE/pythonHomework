def solve(n):
    digits = 0
    temp = n
    while temp > 0:
        digits += 1
        temp = temp // 2
    res = 0
    # 最高位
    if n & (0x1<<(digits-1)):
        res = 0x1 << (digits - 1)
    for i in range(digits-2, -1, -1):
        if n & (0x1<<i) and res & (0x1<<(i+1)):
            continue
        elif n & (0x1<<i) == 0 and res & (0x1<<(i+1)) == 0:
            continue
        else:
            res += 0x1<<i
    print(res)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        solve(num)