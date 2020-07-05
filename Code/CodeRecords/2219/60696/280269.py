
def solve(n):
    i = 0
    while i*i <= n:
        j = 0
        while j <= i:
            if i*i + j*j == n:
                return True
            j += 1
        i += 1
    return False


if __name__ == '__main__':
    n = int(input())
    print(solve(n))