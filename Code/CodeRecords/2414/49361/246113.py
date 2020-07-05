def solution(n):
    if n <= 2:
        return 1.0 / n
    pr = 0.5
    for i in range(2, n + 1):
        pr = 1.0 / i + (i - 2) * 1.0 / i * pr
    return pr


n = int(input())
print("%.5f" % solution(n))