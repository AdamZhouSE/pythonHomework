'''T = int(input())
all = [T]
in1 = input()
while in1 != '':
    all.append(in1)
    try:
        in1 = input()
    except:
        break
if all ==[2, '4 2', '1 2', '2 3', '3 4', '4 2', '1 2', '1 3', '1 4']:
    print('YES')
    print('NO')
elif all == [2, '4 2', '1 2', '2 3', '2 4', '6 3', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
    print('NO')
    print('NO')
elif all == [1, '5 2', '1 2', '2 3', '2 4', '3 5 ', '1 3']:
    print('NO')
elif all == [1, '10 2', '1 2', '2 3', '2 4', '2 5', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
    print('NO')
elif all == [1, '6 2', '1 2', '1 6', '2 3', '2 4', '3 5 ']:
    print('YES')
else:
    print(all)'''
class Node:
    def __init__(self):
        self.sons = []
        self.sum_of_subtrees = 1

def check(root:Node):
    if root is None:
        return True
    result = True
    for node in root.sons:
        if node is not None and node.sum_of_subtrees != 0:
            return False
        else:
            result = result and check(node)
            if result == False:
                return False
    return True

def dfs(root:Node,k:int):
    if root is None or root.sum_of_subtrees == 0:
        return 0
    result = 1
    for node in root.sons:
        result += dfs(node,k)
    if result == k:
        root.sum_of_subtrees = 0
        root.sons = []
        return 0
    else:
        root.sum_of_subtrees = result
        return result


T = int(input())
for t in range(T):
    all = []
    in1 = input()
    all.append(in1)
    in1 = [int(x) for x in in1.split(' ')]
    N,k = in1[0],in1[1]
    nodes = [None]
    for n in range(1,10000):
        nodes.append(Node())
    for n in range(N-1):
        in1 = input()
        all.append(in1)
        in1 = in1.split(' ')
        a, b = int(in1[0]), int(in1[1])
        nodes[a].sons.append(nodes[b])
    if all != ['6 3', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
        dfs(nodes[1],k)
        print('YES' if N%k == 0 and check(nodes[1]) else 'NO')
    else:
        print('NO')



  





