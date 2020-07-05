def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    print(is_perfect(n))