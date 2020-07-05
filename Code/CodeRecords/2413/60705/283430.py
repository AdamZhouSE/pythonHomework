def circularPermutation(n: int, start: int):
    return [start, start ^ 1] if n == 1 else circularPermutation(n - 1, start) + circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]


if __name__ == '__main__':
    n = int(input())
    start = int(input())
    print(circularPermutation(n, start))
