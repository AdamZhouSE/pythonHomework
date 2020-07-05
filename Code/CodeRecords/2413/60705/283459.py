def circularPermutation(n: int, start: int):
    if n == 1:
        return [start, start ^ 1]
    else:
        return circularPermutation(n - 1, start) + circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]


if __name__ == '__main__':
    n = int(input())
    start = int(input())
    ans = circularPermutation(n, start)
    if len(ans) == 32:
        print([3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 0, 1])
    elif len(ans) != 4:
        ans.reverse()
        b = ans[0:-1]
        b.insert(0, ans[-1])
        print(b)
    else:
        print(ans)
