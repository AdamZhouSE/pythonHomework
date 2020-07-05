def solve(n):
    a = int(n / 1000)
    b = (n % 1000) / 100
    c = (n % 100) / 10
    d = n % 10
    res = ''
    if a != 0:
        for i in range(a):
            res += 'M'
    if b != 0:
        if b == 9:
            res += 'CM'
        elif b >= 5:
            res += 'D'
            b -= 5
        if 0 < b < 5:
            if b == 4:
                res += 'CD'
            else:
                for i in range(b):
                    res += 'C'
    if c != 0:
        if c == 9:
            res += 'XC'
        elif c >= 5:
            res += 'L'
            c -= 5
        if 0 < c < 5:
            if c == 4:
                res += 'XL'
            else:
                for i in range(c):
                    res += 'X'
    if d != 0:
        if d == 9:
            res += 'IX'
        elif d >= 5:
            res += 'V'
            d -= 5
        if 0 < d < 5:
            if d == 4:
                res += 'IV'
            else:
                for i in range(d):
                    res += 'I'
    return res


if __name__ == '__main__':
    n = int(input())
    print(solve(n))