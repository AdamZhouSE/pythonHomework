input()
a = list(map(int, input().split(" ")))
b = []
for i in range(0, len(a) - 1):
    b.append(a[i] + a[i + 1])
b.append(a[-1])
for i in b:
    print(i, end=" ")