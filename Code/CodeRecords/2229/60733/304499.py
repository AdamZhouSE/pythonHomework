A = list(map(int, input().split(",")))
res = all(x < A[j] for i, x in enumerate(A) for j in range(i + 2, len(A)))
print(res)
