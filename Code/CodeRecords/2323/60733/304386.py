A = list(map(int, input().split(",")))
K = int(input())
res = max(0, max(A) - min(A) - 2 * K)
print(res)
