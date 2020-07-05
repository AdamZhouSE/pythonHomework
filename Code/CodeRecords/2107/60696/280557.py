def solve(n):
    i = 1
    while i <= n:
        if i == n:
            return True
        i *= 2
    return False


if __name__ == '__main__':
    n = int(input())
    print(solve(n))