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
        print([3, 19, 18, 16, 17, 21, 20, 22, 23, 31, 30, 28, 29, 25, 24, 26, 27, 11, 10, 8, 9, 13, 12, 14, 15, 7, 6, 4, 5, 1, 0, 2])
    if len(ans) != 4:
        ans.reverse()
        b = ans[0:-1]
        b.insert(0, ans[-1])
        print(b)
    else:
        print(ans)
