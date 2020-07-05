def solve(n):
    result = 0
    i = 1
    while i <= n:
        if i % 5 == 0:
            result += 1
        i += 1
    return result


#main-----
n = int(input())
print(solve(n))