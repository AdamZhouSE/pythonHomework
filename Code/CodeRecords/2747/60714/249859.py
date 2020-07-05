def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


a = input()
b = input()
moves = [x for x in input()[2: -2].split("\",\"")]
if a not in moves:
    moves.append(a)
if b not in moves:
    moves.append(b)
data = dict()
for i in range(0, len(moves)):
    for j in range(i + 1, len(moves)):
        diff = 0
        for k in range(0, len(moves[i])):
            if moves[i][k] != moves[j][k]:
                diff += 1
        if diff == 1:
            data.setdefault(moves[i], []).append(moves[j])
            data.setdefault(moves[j], []).append(moves[i])
temp = find_all_paths(data, a, b)
target = min([len(x) for x in temp])
ans = []
for item in temp:
    if len(item) == target:
        ans.append(item)
print(ans)
