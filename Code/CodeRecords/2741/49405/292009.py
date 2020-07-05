a = eval(input())
a.sort()
n = len(a)
ans = 0
for i in range(n):
    l = 1
    for j in range(i + 1, n):
        if a[j] == a[j - 1] + 1:
            l += 1
    ans = max(ans, l)
print(ans)