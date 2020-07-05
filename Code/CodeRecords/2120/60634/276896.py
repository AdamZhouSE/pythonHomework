def solve(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = n % 3
    s = int(n/3)
    if s > 1 and res == 1:
        s -= 1
        res += 3
    return int(pow(3,s)) * res


#main-----
n = int(input())
print(solve(n))