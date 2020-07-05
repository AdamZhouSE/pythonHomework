d = []
n = int(input())
for i in range(n):
    s = ''.join(sorted(list(input().strip())))
    if not s in d: d.append(s)
print(len(d), end='')