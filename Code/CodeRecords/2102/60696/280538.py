def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    cnt = 0
    n = int(input())
    for i in range(2, n):
        if is_prime(i):
            cnt += 1
    print(cnt)