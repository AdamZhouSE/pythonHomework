aa = input()
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
m = 10000000
n = 0
ans = 0
for i in range(len(a)):
    if a[i] < 0:
        n = n + 1
    if abs(a[i]) < m:
        m = a[i]
    if a[i] == 0:
        m = 0
if n % 2 != 0:
    ans = ans + abs(m) + 1
    list.remove(a, m)
for i in range(len(a)):
    if a[i] == 1:
        continue
    elif a[i] == 0:
        ans = ans + 1
    else:
        ans = ans + abs(a[i]) - 1
print(ans)