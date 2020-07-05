l=list(map(int,input().split(",")))
dif=int(input())
d={}
for a in l:
    d[a] = d.get(a - dif, 0) + 1
l=reversed(l)
print(max(d.values()))
