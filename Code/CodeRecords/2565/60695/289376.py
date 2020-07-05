a = input()
a = list(map(int, a.split(",")))
b = input()
b = list(map(int, b.split(",")))
n = []
for i in range(0, len(a)):
    n.append(a[i])
for i in range(0, len(b)):
    n.append(b[i])
n = sorted(n)
if len(n) % 2 == 0:
    print("{:.5f}".format((n[len(n) // 2] + n[len(n) // 2 - 1]) / 2))
else:
    print("{:.5f}".format(n[(len(n) - 1) // 2]))