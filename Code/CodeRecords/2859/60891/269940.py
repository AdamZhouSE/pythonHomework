
n = int(input())
a = []
res = "YES"
for i in range(n):
    a.append(input())
if n % 2 == 0:
    res = "NO"
elif a[0][0] == a[0][1]:
    res = "NO"
else:
    x = a[0][0]
    o = a[0][1]
    is_sym = True
    for i in range(0, n // 2):
        if a[i] != a[n - i - 1]:
            res = "NO"
            is_sym = False
            break
    if is_sym:
        for i in range(0, n // 2 + 1):
            for j in range(n):
                if j == i or j == n - i - 1:
                    if a[i][j] != x:
                        res = "NO"
                        break
                else:
                    if a[i][j] != o:
                        res = "NO"
                        break

print(res)
