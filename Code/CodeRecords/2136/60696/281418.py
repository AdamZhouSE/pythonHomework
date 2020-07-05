def is_valid(n, k):
    while n > 0:
        if n % k != 1:
            return False
        n = int(n/k)
    return True


if __name__ == '__main__':
    n = int(input())
    res = 0
    for i in range(2, n):
        if is_valid(n, i):
            res = i
            break
    print(res)