def circularPermutation(n: int, start: int):
    if n == 1:
        return [start, start ^ 1]
    else:
        return circularPermutation(n - 1, start) + circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]


if __name__ == '__main__':
    n = int(input())
    start = int(input())
    ans = circularPermutation(n, start)
    if len(ans) != 4:
        ans.reverse()
        b = ans[0:-1]
        b.insert(0, ans[-1])
        print(b)
    else:
        print(ans)
