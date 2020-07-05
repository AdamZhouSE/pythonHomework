def solve(n):
    is_negative = 1
    if n < 0:
        is_negative = -1
        n = abs(n)
    original = str(n)[::-1]
    print(is_negative*int(original))


if __name__ == '__main__':
    n = int(input())
    solve(n)