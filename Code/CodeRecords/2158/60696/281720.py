INT_MIN = -int(pow(2, 31))
INT_MAX = int(pow(2, 31)) - 1


def solve(s):
    s = str(s)
    s.strip()
    is_negative = 1
    if s.isspace() or s == '':
        return 0
    if s[0] == '-':
        is_negative = -1
        s = s[1:]
    if '0' <= s[0] <= '9':
        res = 0
        num = '' + s[0]
        i = 1
        while i < len(s) and '0' <= s[i] <= '9':
 INT_MIN = -int(pow(2, 31))
INT_MAX = int(pow(2, 31)) - 1


def solve(s):
    s = str(s)
    s.strip()
    is_negative = 1
    if s.isspace() or s == '':
        return 0
    if s[0] == '-':
        is_negative = -1
        s = s[1:]
    if '0' <= s[0] <= '9':
        res = 0
        num = '' + s[0]
        i = 1
        while i < len(s) and '0' <= s[i] <= '9':
            num += s[i]
            i += 1
        for j in range(0, i):
            res = 10 * res + (ord(s[j]) - ord('0'))
        res = is_negative * res
        res = min(INT_MAX, res)
        res = max(INT_MIN, res)
        return res
    else:
        return 0


if __name__ == '__main__':
    s = input()
    print(solve(s))           num += s[i]
            i += 1
        for j in range(0, i):
            res = 10 * res + (ord(s[j]) - ord('0'))
        res = is_negative * res
        res = min(INT_MAX, res)
        res = max(INT_MIN, res)
        return res
    else:
        return 0


if __name__ == '__main__':
    s = input()[1:-1]
    print(solve(s))