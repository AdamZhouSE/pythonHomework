class Path:
    def __init__(self,paths,values):
        self.paths=paths
        self.values=values
    def cal_value():
        t=0
        for i in values:
            t+=i
        return t
class Tree:
    def __init__(self, root=None, left_child=None, right_child=None,value=None):
        self.root = root
        self.left = left_child
        self.right = right_child
        self.value=value

    def is_empty(self):
        return self.root is None
    
    
    
    
    
    
    
line1 = input().strip()
node_num = int(line1.split()[0])
roo = int(line1.split()[1]) - 1
s = [[0] * node_num for i in range(node_num)]
for i in range(node_num):
    line = input().strip()
    a = int(line.split()[0]) - 1
    b = int(line.split()[1]) - 1
    c = int(line.split()[2]) - 1
    if b >=0:
        s[a][b] = 1
    if c >= 0:
        s[a][c] = 1
tree = produce_a_tree(s, roo)