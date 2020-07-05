def solve(n):
    # 最高为要求不为0
    if n == 1:
        return 10
    count = 9
    for i in range(n - 1):
        count *= (9 - i)
    return count + solve(n - 1)


a = int(input())
print(solve(a))
