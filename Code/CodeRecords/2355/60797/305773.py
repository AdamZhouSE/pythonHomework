import copy


class Node:
    id = None
    value = None
    neighbor = []


class Solution:
    def find2(self, nd: Node, re: int):
        re += nd.value
        if not nd.neighbor:
            return re
        else:
            tmp = nd.neighbor.copy()
            for item in tmp:
                nd.neighbor.remove(item)
                tree[item].neighbor.remove(nd.id)
                re = self.find2(tree[item], re)
                nd.neighbor.append(item)
                tree[item].neighbor.append(nd.id)
            return re

    def find(self, nd: int, nbr: list):  # node, neighbor
        re = tree[nd].value
        if len(nbr) == 0:
            return re
        for item in nbr:
            self.find2(tree[item], re)


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    v = [int(a) for a in input().split()]
    global tree
    tree = {}
    for i in range(n):
        node = Node()
        node.id = i
        node.value = v[i]
        node.neighbor = []
        tree[i] = copy.deepcopy(node)
    total = sum(v)
    edges = []
    for i in range(m):
        [u, v] = [int(a) - 1 for a in input().split()]
        edges.append([u, v])
        tree[u].neighbor.append(v)
        tree[v].neighbor.append(u)
    res = total
    for u, v in edges:
        # tmp = set(tree[v].neighbor)
        # tmp.remove(u)
        tree[u].neighbor.remove(v)
        tree[v].neighbor.remove(u)
        s = Solution()
        # res = min(res, abs(total - 2 * s.find(v, list(tmp))))
        res = min(res, abs(total - 2 * s.find2(tree[v], 0)))
        tree[u].neighbor.append(v)
        tree[v].neighbor.append(u)
    print('Case 1:',res)
