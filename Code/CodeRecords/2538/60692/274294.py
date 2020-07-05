a = input()[1:-1].split(",")
a = [int(i) for i in a]
a.sort()
ans = 0
for i in range(0, len(a) - 1):
    if a[i + 1] - a[i] > 1 and a[i] + 1 > 0:
        ans = a[i] + 1
        break
if ans == 0:
    ans = a[len(a) - 1] + 1
print(ans)