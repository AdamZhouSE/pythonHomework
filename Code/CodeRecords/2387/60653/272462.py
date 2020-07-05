import re
n, m = map(int, input().split())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
for i in range(0, m):
    op, l, r = map(int, input().split())
    tmp = []
    for j in range(l-1, r):
        tmp.append(s[j])
    tmp.sort()
    if op == 1:
        tmp.reverse()
    k = 0
    for j in tmp:
        s[l-1+k] = j
        k += 1
q = int(input())
print(s[q-1])
