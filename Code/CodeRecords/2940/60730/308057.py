def dp(l, r):
    def jud(l, r, cl, cr):
        if (r - l + 1) % (cr - cl + 1) != 0:
            return 0
        for i in range(l, r + 1):
            if s[i] != s[(i - l) % (cr - cl + 1) + cl]:
                return 0
        return 1

    def get(x):
        t = 0
        while x:
            x = x // 10
            t += 1
        return t

    def getch(x):
        tmp = ""
        while (x):
            tmp = chr(x % 10) + tmp
            x = x // 10
        return tmp

    if mark[l][r]:
        return f[l][r]
    if l == r:
        ans[l][r] = s[l]
        return 1
    t = r - l + 1
    for i in range(l, r + 1):
        ans[l][r] += s[i]
    for i in range(l, r):
        tmp = dp(l, i) + dp(i + 1, r)
        if tmp < t:
            t = tmp
            ans[l][r] = ans[l][i] + ans[i + 1][r]
        if jud(i + 1, r, l, i):
            tmp = dp(l, i) + 2 + get((r - i) //(i - l + 1) + 1)
            if tmp < t:
                t = tmp
                ans[l][r] = getch((r - i) // (i - l + 1) + 1) + "(" + ans[l][i] + ")"
    f[l][r] =t
    return f[l][r]


s = input()
l = len(s)
ans = [["" for _ in range(l+1)] for _ in range(l+1)]
mark = [[False for _ in range(l+1)] for _ in range(l+1)]
s = ['' for _ in range(l+1)]
f = [[0 for _ in range(l+1)] for _ in range(l+1)]
dp(0, l - 1)
print(ans[0][l - 1])
