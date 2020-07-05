import heapq

n, c, f = input().split()
n, c, f = int(n), int(c), int(f)
count = int((n-1)/2)

grade, mo = [], []
for i in range(c):
    g, m = input().split()
    g, m = int(g), int(m)
    grade.append(g)
    mo.append(m)
    
dic = dict(zip(grade,mo))
sodi = sorted(dic.items(), key=lambda d:d[0], reverse = False)
nemo = []
for i in sodi:
    nemo.append(i[1])
print(nemo)

ans = 0
for i in range(count, len(sodi)-count):
    left = sum(heapq.nsmallest(count, nemo[:i]))
    right = sum(heapq.nsmallest(count, nemo[i+1:]))
    if left + right + nemo[i] <= f:
        ans = max(ans, sodi[i][0])
    
print(ans,end='')