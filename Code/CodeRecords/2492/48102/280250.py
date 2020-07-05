def get_num(start: int, length: int) -> int:
    end = start + length - 1
    m = []
    count = 0
    for i in range(total):
        if start <= yz[i][0] <= end:
            m.append(yz[i][1])
            count += 1
    p1 = p2 = 0
    while p2 < count and m[p2] - m[p1] + 1 < length:
        p2 += 1
    if p2 >= count or m[p2] - m[p1] + 1 >= length:
        p2 -= 1
    ans = 0
    while p1 <= p2 < count:
        ans = max(ans, p2 - p1 + 1)
        p2 += 1
        while p2 < count and m[p2] - m[p1] + 1 >= length:
            p1 += 1
    return ans


def check(length: int) -> bool:
    for i in range(total):
        if get_num(xz[i][0], length) >= target:
            return True
    return False


def erfen(l: int, r: int) -> int:
    if l == r:
        return l
    mid = (l + r) >> 1
    if check(mid):
        return erfen(l, mid)
    else:
        return erfen(mid + 1, r)


def cmp1(x: list):
    return x[0]


def cmp2(x: list):
    return x[1]


if __name__ == '__main__':
    xz, yz = [], []
    ls = input().split(' ')
    ls = list(map(int, ls))
    target, total = ls[0], ls[1]
    for _ in range(total):
        temp = input().split(' ')
        temp = list(map(int, temp))
        xz.append(temp)
        yz.append(temp)
    xz.sort(key=lambda x: x[0])
    yz.sort(key=lambda x: x[1])
    res = erfen(1, 10000)
    print(res)