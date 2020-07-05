class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root = {}
        wrong = []
        for edge in edges:
            if self.checkcycle(edge, root):
                wrong.append(edge)
            elif edge[1] in root:
                wrong.append([root[edge[1]], edge[1]])
                wrong.append(edge)
                root.pop(edge[1])
            else:
                root[edge[1]] = edge[0]
        for edge in wrong:
            if self.checkcycle(edge, root):
                return edge
            root[edge[1]] = edge[0]
    
    def checkcycle(self, edge, root):
        x = self.getroot(edge[0], root)
        y = self.getroot(edge[1], root)
        if x == edge[1] or y == edge[0] or x == y:
            return True
        return False
    
    def getroot(self, p, root):
        while p in root:
            p = root[p]
        return p


if __name__=="__main__":
    stones=input().strip('[]').split("], [")
    stones=[i.split(",") for i in stones]
    l=len(stones)
    #print(stones)
    for i in range(l):
        for j in range(len(stones[0])):
            stones[i][j]=int(stones[i][j])
    x=Solution().findRedundantDirectedConnection(stones)
    print(x)







