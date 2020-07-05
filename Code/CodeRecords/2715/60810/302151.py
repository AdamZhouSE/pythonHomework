
import collections

n = input()
posi = n[2:-2].split("],[")
for i in range(len(posi)):
    posi[i]=posi[i].split(",")
    posi[i][0] = int(posi[i][0])
    posi[i][1] = int(posi[i][1])
p=collections.defaultdict(set)
for x,_y in posi:
    y=_y+10000
    p[x] |={x}
    p[y] |={y}
    if(p[x]!=p[y]):
        p[x]|=p[y]
        for z in p[y]:
            p[z]=p[x]
print(len(posi)-len(set(id(c) for c in p.values())))