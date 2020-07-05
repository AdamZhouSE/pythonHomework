s = input()
n = len(s)
a = list(map(int, list(input())))
k = int(input())
a[0] = 1 - a[0]
for i in range(1, n):
    a[i] = 1 - a[i] + a[i - 1]
ans = 0
d = []
for i in range(n):
    for j in range(i, n):
        if a[j] - a[i - 1] <= k:
            if not s[i:j + 1] in d:
                d.append(s[i:j + 1])
print(len(d))