def find_father(n):
    newl = [n]
    while n != root:
        if n in leftS:
            ind = leftS.index(n)
        else:
            ind = rightS.index(n)
        newl.append(nodes[ind])
        n = nodes[ind]
    father.append(newl)


inp = input().strip().split(" ")
t = int(inp[0])
root = int(inp[1])
nodes = []
leftS = []
rightS = []
for i in range(t):
    li = input().strip().split(" ")
    nodes.append(int(li[0]))
    leftS.append(int(li[1]))
    rightS.append(int(li[2]))
father = []
li = input().strip().split(" ")
ta1 = int(li[0])
ta2 = int(li[1])
find_father(ta1)
find_father(ta2)
for i in father[0]:
    if i in father[1]:
        print(i)
        break
