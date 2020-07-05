A = input()
B = input()
cnt = 0
for i in range(len(A) - len(B) + 1):
    if A[i:i + len(B)] == B:
        cnt += 1

print(cnt, end='')
