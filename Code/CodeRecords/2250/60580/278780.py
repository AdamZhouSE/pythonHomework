n = int(input())
l = []
for i in range(0, n):
    l.append(list(map(int, input().split(','))))

lrecorder = [[]for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif l[i][0] == l[j][0]:
            lrecorder[i].append('inf')
        else:
            lrecorder[i].append((l[i][1] - l[j][1]) / (l[i][0] - l[j][0]))

maxlen = 0

for i in range(0, n):
    if lrecorder[i].count(max(lrecorder[i], key=lrecorder[i].count)) > maxlen:
        maxlen = lrecorder[i].count(max(lrecorder[i], key=lrecorder[i].count))

print(maxlen+1)
