class Node:
    def __init__(self, id, value=0, father=None):
        self.id = id
        self.father = father
        self.value = value


def find(node, target):
    for i in node:
        if i.id == target:
            return i


def ans(node, S):
    res = []
    for i in range(0, len(node)):
        temp = node[i]
        sum = 0
        length = 0
        while temp is not None:
            sum += temp.value
            temp = temp.father
            length += 1
            if sum == S:
                res.append(length)
    return res


temp = input().split()
n = int(temp[0])
root = Node(int(temp[1]))
node = []
for i in range(1, n + 1):
    node.append(Node(i))
for i in range(n):
    temp = input().split()
    if (int(temp[1]) != 0):
        find(node, int(temp[1])).father = find(node, int(temp[0]))
    if (int(temp[2]) != 0):
        find(node, int(temp[2])).father = find(node, int(temp[0]))
    find(node, int(temp[0])).value = int(temp[3])
S = int(input())
res = ans(node, S)
print(max(res))
