def solve(n):
    a = int(n / 1000)
    b = int((n % 1000) / 100)
    c = int((n % 100) / 10)
    d = int((n % 10))
    if n == 10000:
        return False
    elif n >= 1000:
        if a == 0 or b == 0 or c == 0 or d == 0:
            return False
        if n % a != 0 or n % b != 0 or n % c != 0 or n % d != 0:
            return False
        return True
    elif n >= 100:
        if b == 0 or c == 0 or d == 0:
            return False
        if n % b != 0 or n % c != 0 or n % d != 0:
            return False
        return True
    elif n >= 10:
        if c == 0 or d == 0:
            return False
        if n % c != 0 or n % d != 0:
            return False
        return True
    else:
        if d == 0 or n % d != 0:
            return False
        return True


if __name__ == '__main__':
    left = int(input())
    right = int(input())
    res = []
    for i in range(left, right+1):
        if solve(i):
            res.append(i)
    print(res)
