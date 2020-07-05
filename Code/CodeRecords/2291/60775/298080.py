class Node:
    def __init__(self,left,right,value,visitable):
        self.left = left
        self.right = right
        self.value = value
        self.visitable = visitable

while True:
    try:
        num_v = int(input())
        vs = [int(x) for x in input().split(' ')]
    except Exception:
        break
    vs.sort()
    nodes = []
    #生成哈夫曼树
    for x in vs:
        nodes.append(Node(None,None,x,True))
    while len(nodes) > 1:
        min1 = nodes.pop(0)
        min2 = nodes.pop(0)
        new_nodes = Node(min1,min2,min1.value+min2.value,False)
        #插入正确位置
        for i in range(len(nodes)):
            if nodes[i].value > new_nodes.value:
                nodes.insert(i,new_nodes)
                break
        else:
            nodes.append(new_nodes)
    haff = nodes.pop()
    del new_nodes,nodes,vs
    del min2,min1,num_v,x,i
    #广度遍历得结果
    result = 0
    depth = 0
    queue = [haff]
    this_layer = 1

    while queue != []:
        next_layer = 0
        while this_layer > 0:
            tmp = queue.pop(0)
            if tmp.left != None:
                queue.append(tmp.left)
                next_layer += 1
            if tmp.right != None:
                queue.append(tmp.right)
                next_layer += 1
            if tmp.visitable:
                result += tmp.value * depth
            this_layer -= 1
        this_layer = next_layer
        depth += 1

    print(result)