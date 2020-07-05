def judge(l, r, length):
    if (r - l + 1) % length:
        return 0
    for i in range(1, r - l + 2):
        if s[l + i - 1] != s[l + (i - 1) % length]:
            return 0
    return 1


def digit(num):
    ans = 0
    while num:
        ans += 1
        num = num // 10
    return ans


def change(num):
    s = ""
    while num:
        s = s+(chr(num % 10 + 48))
        num = num // 10

    for i in range(0, len(s) // 2):
        m = i                                       # 'str' object does not support item a
        n = len(s) - 1 - i                          # python字符串修改的算法
        temp = s[n]
        trailer = s[n + 1:] if n + 1 < len(s) else ''
        s = s[0:n] + s[m] + trailer
        s = s[0:m] + temp + s[m + 1:]
    return s


def solve(l, r):
    if f[l][r]:
        return
    if l == r:
        f[l][r] = 1
        c[l][r] = c[l][r] + s[l]
        return

    f[l][r] = r - l + 1
    for i in range(l, r + 1):
        c[l][r] += s[i]
    for i in range(l, r):
        solve(l, i)
        solve(i + 1, r)
        if f[l][r] > f[l][i] + f[i + 1][r]:
            f[l][r] = f[l][i] + f[i + 1][r]
            c[l][r] = c[l][i] + c[i + 1][r]

    for i in range(1, r - l + 1):
        if judge(l, r, i):
            solve(l, l + i - 1)
            if f[l][r] > f[l][l + i - 1] + 2 + digit((r - l + 1) // i):
                f[l][r] = f[l][l + i - 1] + 2 + digit((r - l + 1) // i)
                c[l][r] = change((r - l + 1) // i) + "(" + c[l][l + i - 1] + ")"


s = input()
l = len(s)
f = [[0 for _ in range(110)] for _ in range(110)]
c = [["" for _ in range(110)] for _ in range(110)]
solve(0, l - 1)
print(c[0][l - 1])
