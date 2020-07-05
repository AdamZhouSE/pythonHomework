class Node:
    def __init__(self, value, father=None, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value
        self.father = father


def getDepth(root):
    if (root == None):
        return 0
    if (root.leftchild == None and root.rightchild == None):
        return 1
    else:
        return max(getDepth(root.leftchild) + 1, getDepth(root.rightchild) + 1)


def getWidth(root):
    if (root == None):
        return 0
    queue = [root]
    maxWidth = 1
    while (True):
        l = len(queue)  # 当前层节点个数
        if (l == 0):  # 当前层没有节点
            break
        while (l > 0):
            temp = queue.pop(0)
            l -= 1
            if temp.leftchild != None:
                queue.append(temp.leftchild)
            if temp.rightchild != None:
                queue.append(temp.rightchild)
        maxWidth = max(len(queue), maxWidth)
    return maxWidth

def getDistance(u,v):
    Upath="" + str(u.value)
    Vpath="" + str(v.value)
    temp = u
    while(temp.father!=None):
        temp = temp.father
        Upath += str(temp.value)
    temp = v
    while (temp.father != None):
        temp = temp.father
        Vpath += str(temp.value)
    for i in range(len(Upath)):
        for j in range(len(Vpath)):
            if(Upath[i]==Vpath[j]):
                res = (i)*2+j
                return res

def ans():
    n = int(input())
    nodes = []
    for i in range(0, n + 1):
        nodes.append(Node(i))
    for i in range(1, n):
        temp = input().split()
        if (nodes[int(temp[0])].leftchild == None):
            nodes[int(temp[0])].leftchild = nodes[int(temp[1])]
            nodes[int(temp[1])].father = nodes[int(temp[0])]
        else:
            nodes[int(temp[0])].rightchild = nodes[int(temp[1])]
            nodes[int(temp[1])].father = nodes[int(temp[0])]
    temp = input().split()
    u = nodes[int(temp[0])]
    v = nodes[int(temp[1])]
    distance = getDistance(u,v)
    width = getWidth(nodes[1])
    depth = getDepth(nodes[1])
    print(depth)
    print(width)
    print(distance,end="")


if __name__ == '__main__':
    ans()
