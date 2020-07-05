n = int(input())
name = []
score = []
j = 0
m = 0
ans = ""
for i in range(0, n):
    a = input().split()
    ni = a[0]
    si = int(a[1])
    if name.count(ni) > 0:
        score[name.index(ni)] += si
    else:
        name.append(ni)
        score.append(si)
    if score[name.index(ni)] > m:
        ans = ni
        m = score[name.index(ni)]

print(ans)