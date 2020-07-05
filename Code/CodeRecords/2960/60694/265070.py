m, n = map(int, input().split())
A, B = input(), input()
k = 0
indexs = []
flag = True
for i in range(n-m+1):
    substr = B[i:i+m]
    for j in range(m):
        if substr[j] == '*' or A[j] == '*' or substr[j] == A[j]:
            flag = True
        else:
            flag = False
            break
        if j == m-1 and flag:
            indexs.append(i+1)
            k += 1
            flag = False
print(k)
print(*indexs, end=" ")
print()
