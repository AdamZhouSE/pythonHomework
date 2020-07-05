line = eval(input())
line.reverse()
tar = set()
for i in range(1,len(line)+1):
    tar.add(i)
for i in range(len(line)):
    temp = []
    for j in range(len(line)):
        temp.append(line[j])
    del temp[i]
    start = temp[0][0]
    now = set()
    stack = []
    stack.append(start)
    while len(stack) != 0:
        node = stack.pop()
        now.add(node)
        for item in temp:
            if item[0] == node and item[1] not in stack and item[1] not in now:
                stack.append(item[1])
            if item[1] == node and item[0] not in stack and item[0] not in now:
                stack.append(item[0])
    if now == tar:
        print(line[i])
        break