roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def solve(s):
    n = len(s)
    res = 0
    i = n-1
    while i >= 0:
        res += roman_num[s[i]]
        if i >= 1 and s[i-1] == 'I' and (s[i] == 'V' or s[i] == 'X'):
            res -= 1
            i -= 2
        elif i >= 1 and s[i-1] == 'X' and (s[i] == 'L' or s[i] == 'C'):
            res -= 10
            i -= 2
        elif i >= 1 and s[i-1] == 'C' and (s[i] == 'D' or s[i] == 'M'):
            res -= 100
            i -= 2
        else:
            i -= 1
    return res


if __name__ == '__main__':
    s = input()
    print(solve(s))

