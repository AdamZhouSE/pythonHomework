equations=input().split(',')
list1=[]
for i in range(0,len(equations)):
    if i==0:
        list1.append(equations[0][2:(len(equations[0])-1)])
    elif i==len(equations)-1:
        list1.append(equations[i][1:(len(equations[0])-2)])
    else:
        list1.append(equations[i][1:(len(equations[0]) - 1)])
equations=list1
graph = [[] for _ in range(0,26)]

for eqn in equations:
    if eqn[1] == '=':
        x = ord(eqn[0]) - ord('a')
        y = ord(eqn[3]) - ord('a')
        graph[x].append(y)
        graph[y].append(x)

color = [None] * 26
t = 0
for start in range(0,26):
    if color[start] is None:
        t += 1
        stack = [start]
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if color[nei] is None:
                    color[nei] = t
                    stack.append(nei)
flag=True
for eqn in equations:
    if eqn[1] == '!':
        x = ord(eqn[0]) - ord('a')
        y = ord(eqn[3]) - ord('a')
        if x == y:
            print("false")
            flag=False
        elif color[x] is not None and color[x] == color[y]:
            print("false")
            flag=False
if flag:
    print("true")
