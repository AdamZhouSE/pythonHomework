s = input()
n = len(s)
ss = s[1:n-1]
flag = False
t = []
temp = []
for i in range(0, len(ss)):
    if ss[i] == '[':
        temp = []
    elif ss[i] == ']':
        t.append(temp)
    elif ss[i] != ',':
        temp.append(int(ss[i]))
high = len(t)
wide = len(t[0])
col = wide
ans = [[0 for i in range(0, wide)]for j in range(0, high)]
res = []

for i in range(high):
    for j in range(col - 1, -1, -1):
        lst = []
        i1, j1 = i, j
        while i1 <= high - 1 and j1 <= wide - 1:
            lst.append(t[i1][j1])
            i1 += 1
            j1 += 1
        lst.sort()
        for k in lst:
            res.append(k)
        if i == 0 and j == 0:
            col = 1
k = 0
col = wide
for i in range(high):
    for j in range(col - 1, -1, -1):
        i1, j1 = i, j
        while i1 <= high - 1 and j1 <= wide - 1:
            ans[i1][j1] = res[k]
            i1 += 1
            j1 += 1
            k += 1
        if i == 0 and j == 0:
            col = 1
print(ans)