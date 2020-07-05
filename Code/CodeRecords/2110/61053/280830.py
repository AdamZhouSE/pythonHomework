def is_ugly(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            break
    while n > 1:
        if n % 3 == 0:
            n = n / 3
        else:
            break
    while n > 1:
        if n % 5 == 0:
            n = n / 5
        else:
            break
    return n == 1

if __name__ == "__main__":
    n = int(input())
    print(is_ugly(n))