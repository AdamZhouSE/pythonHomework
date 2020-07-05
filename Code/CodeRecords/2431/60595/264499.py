import math
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
    S,P=map(int,input().split())
    located=[]
    mat = []
    for i in range(0, P):
        line = []
        for j in range(0, P):
            line.append(99999)
        mat.append(line)
    for i in range(0,P):
        located.append(eval("["+input().replace(" ",",")+"]"))
    for i in range(0,P):
        for j in range(i+1,P):
            d=distance(located[i][0]-located[j][0],located[i][1]-located[j][1])
            mat[i][j]=d
            mat[j][i]=d
    graph=Graph(mat)
    res=graph.prim()
    res.sort(key=lambda x:x[2],reverse=True)
    try:
        v=(S*(S-1))//2
        x=res[v][2]
        print('%.2f'%x,end="")
    except:
        print(P,S,res)
def distance(a,b):
    return math.sqrt(a*a+b*b)
if __name__ == "__main__":
    Test()