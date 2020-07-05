def get_F(s):
    F = [-1]
    for i, v in enumerate(s):
        k = F[i]
        while k != -1 and s[k] != s[i]:
            k = F[k]
        F.append(k + 1)
    return F


def kmp(s1, s2):
    F = get_F(s2)
    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j = F[j]
        if j == len(s2):
            return True
        if j == -1:
            i += 1
            j += 1
    return False


def a3():
    n, m = [int(x) for x in input().strip().split(' ')]
    s = input()
    ret = []
    for i in range(m):
        a, b, c, d = [int(x) for x in input().strip().split(' ')]
        s1, s2 = s[a - 1:b], s[c - 1:d]
        low, high, res = 0, len(s2) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            flag = kmp(s1, s2[:mid + 1])
            if flag:
                low = mid + 1
                res = max(res, mid)
            else:
                high = mid - 1
        ret.append(res + 1)
    print('\n'.join([str(r) for r in ret]))


if __name__ == '__main__':
    a3()
