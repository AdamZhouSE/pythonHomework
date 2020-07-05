A = eval(input())
K = int(input())

min_len = 10000
for i in range(1, len(A) + 1):
    for j in range(len(A) - i + 1):
        subA = A[j: j+i]
        if sum(subA) >= K:
            if len(subA) < min_len:
                min_len = len(subA)
if min_len == 10000:
    print(-1)
else:
    print(min_len)
