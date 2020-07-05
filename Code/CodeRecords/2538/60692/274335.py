a = input()[1:-1].split(",")
a = [int(i) for i in a]
a.sort()
ans = 1
for i in a:
    if i <= 0:
        a.remove(i)
if ans < a[0]:
    print(ans)
else:
    for j in range(0, len(a) - 1):
        if a[j + 1] - a[j] > 1:
            ans = a[j] + 1
            break
    if ans == 1:
        ans = a[len(a) - 1] + 1
    print(ans)
