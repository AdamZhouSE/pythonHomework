l=list(map(int,input().split(",")))
dif=int(input())
d={}
for a in l:
    d[a] = d.get(a - dif, 0) + 1
l=reversed(l)
e={}
for a in l:
    e[a] = e.get(a - dif, 0) + 1
print(max(max(e.values()),max(d.values())))
