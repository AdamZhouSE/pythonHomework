def equationsPossible( equations):
        graph = [[] for _ in xrange(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [None] * 26
        t = 0
        for start in xrange(26):
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
                if x == y: return 'false'
                if color[x] is not None and color[x] == color[y]:
                    return 'false'
        return 'true'
s=input()
s=s[1:len(s)-1]
sl=s.split(',')
l=[]
for x in sl:
    l.append(x[1:len(x)-1])
print(equationsPossible(l))