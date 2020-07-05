a = eval(input())
ans = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i]+a[k] > a[j] and a[i]+a[j] > a[k] and a[k]+a[j] > a[i]:
                if a[i] + a[k] + a[j] > ans:
                    ans = a[i] + a[k] + a[j]
print(ans)