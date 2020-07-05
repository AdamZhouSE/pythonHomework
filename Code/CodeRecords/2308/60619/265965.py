def in_dex(fa):
    ind = nodes.index(fa)
    if leftSon[ind] != 0:
        in_dex(leftSon[ind])
    string.append(fa)
    if rightSon[ind] != 0:
        in_dex(rightSon[ind])


li = input().split(" ")
length = int(li[0])
root = int(li[1])
nodes = []
leftSon = []
rightSon = []
for i in range(length):
    nodes.append(0)
    leftSon.append(0)
    rightSon.append(0)
for i in range(length):
    inp = input().split(" ")
    nodes[i] = int(inp[0])
    leftSon[i] = int(inp[1])
    rightSon[i] = int(inp[2])
string = []
in_dex(root)
target = int(input())
result = string.index(target)
if result == length - 1:
    print(0)
else:
    print(string[result+1])