def solve(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        return solve(n/2, cnt+1)
    else:
        return min(solve(n+1, cnt+1), solve(n-1, cnt+1))


if __name__ == '__main__':
    n = int(input())
    print(solve(n, 0))