def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums_str1 = nums_str.replace('\"', '')

    nums = [str(n) for n in nums_str1.split(",")];
    return nums;


def equationsPossible(equations):
    graph = [[] for _ in range(26)]

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
            if x == y:
                return False  # lee
            if color[x] is not None and color[x] == color[y]:
                return False
    return True

l = getInput()
t = equationsPossible(l)
if t == True:
    print('true')
else:
    print('false')