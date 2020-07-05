global s, ss
global n, f


def jug(l, r):
    for i in range(1, int((r - l + 1) / 2 + 1)):
        if (r - l + 1) % i == 0:
            bo = 0
            j = l
            while j + i <= r:
                if s[j] != s[j + i]:
                    bo = 1
                    break
                j = j + 1
            if bo == 0:
                return i
    return -1


def dfs(left, right):
    if f[left][right] != -1:
        return f[left][right]
    if left == right:
        f[left][right] = 1
        ss[left][right] = s[left]
        return 1
    re = 1e5
    pos = 0
    temp = 0
    for i in range(left, right):
        temp = dfs(left, i) + dfs(i + 1, right)
        if re > temp:
            re = temp
            pos = i
    ss[left][right] = ss[left][pos] + ss[pos + 1][right]
    le = jug(left, right)
    if le != -1:
        t = ''
        nes = ''
        temp = int((right - left + 1) / le)
        while temp != 0:
            ch = chr(temp % 10 + 48)
            t = t + ch
            temp = int(temp / 10)
        t = t[::-1]
        nes = t + "(" + ss[left][left + le - 1] + ")"
        if len(nes) < re:
            re = len(nes)
            ss[left][right] = nes
    f[left][right] = re
    return re


if __name__ == "__main__":
    f = [[-1] * 105 for i in range(105)]
    ss = [[""] * 105 for j in range(105)]
    s = input()
    n = len(s)
    dfs(0, n - 1)
    print(ss[0][n - 1])
