
import collections
cnt = int(input())
li = []
liOfM = []
liOfN = []
for i in range(cnt):
    liOfN.append(int(input()))
    li.append(input().split(" "))
    liOfM.append(int(input()))

for i in range(cnt):
    c = collections.Counter(li[i])
    m = liOfM[i]
    n = liOfN[i]
    sortedC = sorted(c.items(), key=lambda kv: (kv[1], kv[0]))
    k = 0
    for j in sortedC:
        m -= j[1]
        if m < 0:
            break
        elif m == 0:
            k += 1
            break
        else:
            k += 1
    print(len(sortedC) - k)

