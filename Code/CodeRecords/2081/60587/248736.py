A = input()
B = input()
res = 0
for i in range(0, len(A) - len(B) + 1):
    if B[0] == A[i]:
        if B == A[i:i + len(B)]:
            res += 1
print(res, end="")
