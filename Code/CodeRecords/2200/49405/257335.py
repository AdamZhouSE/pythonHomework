s = input()
n = len(s)
a = [0] + list(map(int, list(input())))
k = int(input())
for i in range(1, n + 1):
    a[i] = 1 - a[i] + a[i - 1]
ans = 0
d = []
for i in range(n):
    for j in range(i, n):
        if a[j + 1] - a[i] <= k:
            if not s[i:j + 1] in d:
                d.append(s[i:j + 1])
print(len(d))