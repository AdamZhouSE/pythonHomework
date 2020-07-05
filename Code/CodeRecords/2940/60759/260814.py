def judge(l, r, length):
    # 判断string[l][r]内是否由长度为length的字符串重复若干次组成
    if (r - l + 1) % length:
        return False
    for i in range(1, r - l + 2):
        if string[l + i - 1] != string[l + (i - 1) % length]:
            return False
    return True


def solve(l, r):
    # 得到string[l][r]的最佳方案
    # print(l, r)
    if f[l][r]:
        return
    elif l == r:
        f[l][r] = 1
        c[l][r] = string[l]
        return
    c[l][r] = string[l:r+1]
    f[l][r] = r - l + 1
    for i in range(l, r):
        solve(l, i)
        solve(i + 1, r)
        if f[l][r] > f[l][i] + f[i+1][r]:
            f[l][r] = f[l][i] + f[i+1][r]
            c[l][r] = c[l][i] + c[i+1][r]
    for i in range(1, r - l + 1):
        if judge(l, r, i):
            str_d = str((r - l + 1) // i)
            if f[l][r] > len(str_d) + 2 + i:
                f[l][r] = len(str_d) + 2 + i
                c[l][r] = str_d + '(' + string[l:l+i] + ')'


string = input()
lgt = len(string)
f = [[0 for i in range(lgt)] for j in range(lgt)]
c = [['' for m in range(lgt)] for n in range(lgt)]
solve(0, lgt - 1)
print(c[0][lgt - 1])
