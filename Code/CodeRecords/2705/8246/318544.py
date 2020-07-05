import json


class Solution:
    def findRedundantDirectedConnection(self, edges):
        cnt = set()
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                cnt.add(edges[i][j])
        N = len(cnt)
        parent = [i + 1 for i in range(N)]
        indegree = [0] * N  
        for x, y in edges:
            indegree[y - 1] += 1

        def find(parent, x):
            if parent[x - 1] == x:
                return x
            return find(parent, parent[x - 1])

        def union(parent, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)
            if x_root == y_root:
                return [x, y]
            elif x_root != y_root:
                parent[y_root - 1] = x_root  

        if 2 in indegree: 
            dual_node = indegree.index(2) + 1
            dual_edge = []
            for x, y in edges: 
                if y == dual_node:
                    dual_edge.append([x, y])

            for edge in dual_edge[::-1]:  
                flag = 0  
                for e in edges:
                    if e != edge:
                        if union(parent, e[0], e[1]):
                            flag = 1
                if flag == 1:  
                    return dual_edge[0]
                else:  
                    return edge
        else:  
            for x, y in edges:
                if union(parent, x, y):
                    return union(parent, x, y)


def stringToInt2dArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            edges = stringToInt2dArray(line)

            ret = Solution().findRedundantDirectedConnection(edges)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


main()
