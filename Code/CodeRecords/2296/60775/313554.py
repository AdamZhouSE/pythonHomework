class Node:
    def __init__(self,left,right,value):
        self.left = left
        self.right = right
        self.value = value

def find_max_len(root:Node,sum):
    summap = {}
    summap[0] = 0
    return pre(root,sum,0,1,0,summap)

def pre(root:Node,sum,presum,level,maxlen,summap:dict):
    if root is None:
        return maxlen
    cursum = presum+root.value
    if not (cursum in summap):
        summap[cursum] = level
    if (cursum-sum) in summap:
        maxlen = max(level-summap[cursum-sum],maxlen)
    maxlen = pre(root.left,sum,cursum,level+1,maxlen,summap)
    maxlen = pre(root.right,sum,cursum,level+1,maxlen,summap)
    if level == summap[cursum]:
        summap.pop(cursum)
    return maxlen

in1 = input().split(' ')
n = int(in1[0])
root = int(in1[1])
nodes = [None]
for i in range(n):
    nodes.append(Node(None,None,0))
for i in range(n):
    in1 = [int(x) for x in input().split(' ')]
    cnode = nodes[in1[0]]
    cnode.left = nodes[in1[1]]
    cnode.right = nodes[in1[2]]
    cnode.value = in1[3]
k = int(input())

print(find_max_len(nodes[root],k))
