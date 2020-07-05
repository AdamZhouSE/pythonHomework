m, n = map(int, input().split())
A = input()
B = input()
ans = []
flag = True
if m > n:
    print(0)
    exit()
for i in range(n - m + 1):
    for j in range(m):
        flag = True
        if A[j] == B[i + j] or A[j] == "*" or B[i + j] == "*":
            continue
        else:
            flag = False
            break
    if flag:
        ans.append(i + 1)
print(len(ans))
print(" ".join(map(str, ans)),end=' ')
print()
