def gcd(x, y):
    if y == 1:
        return x - 1
    if x == 0 or y == 0 or x == y:
        return 10 ** 8
    return gcd(y, x % y) + x//y


if __name__ == '__main__':
    n = int(input())
    ans = n - 1
    for i in range(2, n):
        ans = min(gcd(n, i), ans)
    print(ans)
