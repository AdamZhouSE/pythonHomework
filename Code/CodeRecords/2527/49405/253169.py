res = eval(input())
v = int(input())
p = int(input())
d = int(input())
re = []
for r in res:
    if r[2] >= v and r[3] <= p and r[4] <= d:
        re.append(r)
re.sort(key=lambda x: (x[1], x[0]), reverse=True)
print([r[0] for r in re])