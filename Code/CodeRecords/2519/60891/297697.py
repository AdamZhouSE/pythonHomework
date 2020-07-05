a = eval(input())
a.sort(reverse=True)
ans = -1
for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            if a[i] < a[j] + a[k]:
                ans = a[i] + a[j] + a[k]
print(ans)