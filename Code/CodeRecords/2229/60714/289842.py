A = [int(x) for x in input().split(",")]
m = 0
n = 0
for i in range(0, len(A)):
    if A[i] - i > 0:
        m = m + A[i] - i
for i in range(1, len(A)):
    if A[i - 1] > A[i]:
        n += 1
if m == n:
    print(True)
else:
    print(False)
