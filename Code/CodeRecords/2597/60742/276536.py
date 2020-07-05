beauty = []
cost = []
s = [int(i) for i in input().split()]
while s[0]!=-1:
    if s[0]==1:
        if s[2] not in cost:
            beauty.append(s[1])
            cost.append(s[2])
    elif s[0]==2:
        if cost:
            idx = cost.index(max(cost))
            cost.pop(idx)
            beauty.pop(idx)
    else:
        if cost:
            idx = cost.index(min(cost))
            cost.pop(idx)
            beauty.pop(idx)
    s = [int(i) for i in input().split()]
res1 = 0
res2 = 0
for i in beauty:
    res1 += i
for i in cost:
    res2 += i
print(res1,res2,end='')