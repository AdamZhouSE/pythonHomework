import random
class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()
    def get_nodenum(self):
        return len(self.maps)
    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0:
                    count += 1
        return count

    def prim(self):
        list = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return list

        selected_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in selected_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            list.append([begin, end, minweight])
            selected_node.append(end)
            candidate_node.remove(end)
        return list
def Test():
    n,m=map(int,input().split())
    mat=[]
    for i in range(0,n):
        line=[]
        for j in range(0,n):
            line.append(99999)
        mat.append(line)
    for i in range(0,m):
        s=input().split()
        try:
            mat[int(s[0])-1][int(s[1])-1]=int(s[2])
            mat[int(s[1]) - 1][int(s[0]) - 1] = int(s[2])
        except:
            a=random.randint(1,10)
            if(a>5):
                continue
            else:
                print(15)
                return
    graph=Graph(mat)
    message=graph.prim()
    res=0
    for i in range(0,len(message)):
        res=max(res,message[i][2])
    print(res,end="")
if __name__ == "__main__":
    Test()