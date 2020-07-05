equations = eval(input())

graph = [[] for _ in range(26)]
res = "true"

for eqn in equations:
    if eqn[1] == '=':
        x = ord(eqn[0]) - ord('a')
        y = ord(eqn[3]) - ord('a')
        graph[x].append(y)
        graph[y].append(x)

color = [None] * 26
t = 0
for start in range(26):
    if color[start] is None:
        t += 1
        stack = [start]
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if color[nei] is None:
                    color[nei] = t
                    stack.append(nei)

for eqn in equations:
    if eqn[1] == '!':
        x = ord(eqn[0]) - ord('a')
        y = ord(eqn[3]) - ord('a')
        if x == y: res = "false"
        if color[x] is not None and color[x] == color[y]:
            res = "false"

print(res)