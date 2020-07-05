def search(edgedict, start, end, k):
    if start not in edgedict:
        return -1
    if k == 0:
        return -1
    elif k == 1:
        if end in edgedict[start][0]:
            return edgedict[start][1][edgedict[start][0].index(end)]
        else:
            return -1
    else:
        res = []
        for index in range(len(edgedict[start][0])):
            s = search(edgedict, edgedict[start][0][index], end, k-1)
            if s != -1:
                res.append(edgedict[start][1][index] + s)
        if len(res) == 0:
            return -1
        return min(res)


n = int(input())
edges = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
edgedict = {}
for x in edges:
    if x[0] not in edgedict:
        edgedict[x[0]] = [[x[1]], [x[2]]]
    else:
        edgedict[x[0]][0].append(x[1])
        edgedict[x[0]][1].append(x[2])
src = int(input())
dst = int(input())
k = int(input())
print(search(edgedict, src, dst, k + 1))
