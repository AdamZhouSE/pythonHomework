def circularPermutation(n: int, start: int):
    if n == 1:
        return [start, start ^ 1]
    else:
        return circularPermutation(n - 1, start) + circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]


if __name__ == '__main__':
    n = int(input())
    start = int(input())
    ans = circularPermutation(n, start)
    ans.reverse()
    ans = ans[1:].insert(ans[0])
    print(ans)
