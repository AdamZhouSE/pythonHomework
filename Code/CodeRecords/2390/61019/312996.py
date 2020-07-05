read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n, ans = 0, 0
binary, fac = [1] * 20, [1] * 20
ns = []


# Check from ns[x] to ns[x+2^k]
def check(x, k):
    for i in range(binary[k] - 1):
        if ns[x + i] + 1 != ns[x + i + 1]:
            return False
    return True


def swap(x, y, length):
    for i in range(binary[length]):
        ns[x + i], ns[y + i] = ns[y + i], ns[x + i]


def dfs(k, cnt):
    global ans
    if k == n + 1:
        ans += fac[cnt]
        return
    t1, t2 = -1, -1
    for i in range(0, binary[n], binary[k]):
        if not check(i, k):
            if t1 == -1:
                t1 = i
            elif t2 == -1:
                t2 = i
            else:
                return
    if t1 == -1 and t2 == -1:
        dfs(k + 1, cnt)
    elif t2 == -1:
        swap(t1, t1 + binary[k - 1], k - 1)
        dfs(k + 1, cnt + 1)
        swap(t1, t1 + binary[k - 1], k - 1)
    else:
        for x in range(2):
            for y in range(2):
                swap(t1 + x * binary[k - 1], t2 + y * binary[k - 1], k - 1)
                if check(t1, k) and check(t2, k):
                    dfs(k + 1, cnt + 1)
                    swap(t1 + x * binary[k - 1], t2 + y * binary[k - 1], k - 1)
                    continue
                swap(t1 + x * binary[k - 1], t2 + y * binary[k - 1], k - 1)


if __name__ == '__main__':
    for i in range(1, 20):
        binary[i] = binary[i - 1] * 2
    for i in range(1, 20):
        fac[i] = fac[i - 1] * i
    n = read()
    ns = read_line()
    dfs(1, 0)
    print(ans)
