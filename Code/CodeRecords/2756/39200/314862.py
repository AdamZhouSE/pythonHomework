n = int(input())
re = []
be = []
str1 = input()[2:-2]
if "],[" in str1:
    re = [[int(y) for y in x.split(",")] for x in str1.split("],[")]
elif "," in str1:
    re = [[int(y) for y in str1.split(",")]]
str1 = input()[2:-2]
if "],[" in str1:
    be = [[int(y) for y in x.split(",")] for x in str1.split("],[")]
elif "," in str1:
    be = [[int(y) for y in str1.split(",")]]
red = {i : [] for i in range(n)}
bed = {i : [] for i in range(n)}
for e in re:
    red[e[0]].append(e[1])
for e in be:
    bed[e[0]].append(e[1])

def search(cur, target, visited, rb):
    if cur in visited:
        return -1
    if cur == target:
        return 0
    retv = []
    newvisited = visited.copy()
    newvisited.append(cur)
    if rb == 0:
        #red edge
        for x in red[cur]:
            d = search(x, target, newvisited, 1)
            if d != -1:
                retv.append(1 + d)
    else:
        #blue edge
        for x in bed[cur]:
            d = search(x, target, newvisited, 0)
            if d != -1:
                retv.append(1 + d)
    if retv == []:
        return -1
    return min(retv)


res = []
for i in range(n):
    dr = search(0, i, [], 0)
    db = search(0, i, [], 1)
    if dr == -1 and db == -1:
        res.append(-1)
    elif dr == -1:
        res.append(db)
    elif db == -1:
        res.append(dr)
    else:
        res.append(min(db, dr))
print(res)
