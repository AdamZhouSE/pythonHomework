nodes = eval(input())
res = []
for i in range(0,len(nodes)):
    num1 = 0
    num2 = 0
    for j in range(0,len(nodes)):
        if j == i: continue
        if nodes[i][0] == nodes[j][1]:
            mark1 = nodes[i][0]
            num1 = 1
        if nodes[i][1] == nodes[j][1]:
            mark2 = nodes[i][1]
            num2 = 1
        if  nodes[j][1] == nodes[0][0]:
            num1 = 1
            num2 = 1
            mark1 = nodes[j][0]
            mark2 = nodes[j][1]
        if num1 and num2 and not [mark1,mark2] in res:
            num1 = 0
            num2 = 0
            res.append([mark1,mark2])
print(res[len(res)-1])
