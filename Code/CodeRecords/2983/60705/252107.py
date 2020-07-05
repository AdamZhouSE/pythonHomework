# 判断能否构成回文串
def f(string, n):
    b = []
    for i in range(0, 26):
        b.append(chr(97 + i))

    k = 0
    for i in range(0, 26):
        t = 0
        for j in range(0, n):
            if string[j] == b[i]:
                t += 1
            if t % 2 != 0:
                k += 1
    if k > 1:
        return False
    else:
        return True


def step(n, s, s1, res):
    for i in range(n // 2):
        if s[i:].count(s[i]) != 1:
            temp = s1[:n - i].index(s[i])  # 是要移动的步数
            s1.pop(temp)
            res += temp
            s = s1[::-1]
        else:
            res += n // 2 - i
            s[i] = None
            s1 = s[::-1]
    return res


if __name__ == '__main__':
    n = int(input())
    s = list(input())
    if f(str(s), n):
        print("Impossible")
    else:
        s1 = s[::-1]
        res = 0
        print(step(n, s, s1, res))
