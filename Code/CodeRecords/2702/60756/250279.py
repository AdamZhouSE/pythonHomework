class UnionFindSet(object):
    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def __len__(self):
        length=0
        for node in self.father_dict:
            if node==self.father_dict[node]:
                length+=1
        return length

    def find_head(self, node):
        father = self.father_dict[node]
        if(node != father):
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        return self.find_head(node_a) == self.find_head(node_b)

    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return

        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size



row=list(input())
rowL=1
grid=[row]
try:
    while True:
        column=list(input())
        if not column:break
        rowL+=1
        grid.append(column)
except EOFError:pass
columnL=len(row)
pointList=[(-1,-1)]
for i in range(rowL):
    for j in range(columnL):
        pointList.append((i,j))
islands=UnionFindSet(pointList)
def extendUnion(point,lpoint,gird):
    x,y=point
    if x<rowL and y<columnL:
        if gird[x][y]=='0':
            islands.union((-1,-1),point)
            extendUnion((x + 1, y), (x+1,y), grid)
            extendUnion((x, y + 1), (x,y+1), grid)
        else:
            islands.union(lpoint,point)
            extendUnion((x+1,y),point,grid)
            extendUnion((x,y+1),point,grid)
extendUnion((0,0),(0,0),grid)
print(len(islands)-1)