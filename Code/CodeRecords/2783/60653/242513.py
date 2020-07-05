n = int(input())
name = []
score = []
j = 0
for i in range(0, n):
    a = input().split()
    ni = a[0]
    si = int(a[1])
    if name.count(ni) > 0:
        score[name.index(ni)] += si
    else:
        name.append(ni)
        score.append(si)
sn_zip = zip(score, name)
sn_zip = sorted(sn_zip, key=lambda x: x[0])
print(sn_zip[len(sn_zip) - 1][1])
