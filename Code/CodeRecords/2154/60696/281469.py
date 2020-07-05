def solve(n):
    original = str(abs(n))
    i = 0
    j = len(original)-1
    while i < j:
        if original[i] != original[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    n = int(input())
    print(solve(n))