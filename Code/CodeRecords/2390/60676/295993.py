MaxN = 1 << 13
a = [0 for i in range(MaxN)]
po = [0 for i in range(13)]


def check(k: int):
    for i in range(1 << (n - k)):
        if a[i * (1 << k) + 1] + (1 << (k - 1)) != a[i * (1 << k) + (1 << (k - 1)) + 1]:
            return 0
    return 1


def swap(i: int, j: int, k: int):
    for m in range(k):
        tmp = a[i + m]
        a[i + m] = a[j + m]
        a[j + m] = tmp


def dfs(now: int, num: int):
    global ans
    if now and not check(now):
        return
    if now == n:
        ans += po[num]
        return
    dfs(now + 1, num)
    tmp = [0, 0, 0, 0, 0]
    tot = 0
    for i in range(1, (1 << (n - now)) + 1, 2):
        if a[i * (1 << now) + 1] != a[(i - 1) * (1 << now) + 1] + (1 << now):
            if tot == 4:
                return
            tot += 1
            tmp[tot] = i
            tot += 1
            tmp[tot] = i + 1
    if not tot:
        return
    for i in range(1, tot + 1):
        for j in range(i + 1, tot + 1):
            swap((1 << now) * (tmp[i] - 1) + 1, (1 << now) * (tmp[j] - 1) + 1, 1 << now)
            dfs(now + 1, num + 1)
            swap((1 << now) * (tmp[i] - 1) + 1, (1 << now) * (tmp[j] - 1) + 1, 1 << now)


if __name__ == '__main__':
    po[0] = 1
    for i in range(1, 13):
        po[i] = po[i - 1] * i
    n = eval(input())
    arr = input().split()
    ans = 0
    for i in range(1, (1 << n) + 1):
        a[i] = int(arr[i-1])
    dfs(0, 0)
    print(ans)