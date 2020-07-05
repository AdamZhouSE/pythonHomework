def s14():

    def solve(n):
        if n <= 11:
            return n
        if n // 2 + n // 3 + n // 4 > n:
            return solve(n // 2) + solve(n // 3) + solve(n // 4)
        else:
            return n

    t = int(input())
    for i in range(t):
        x = int(input())
        print(solve(x))


s14()