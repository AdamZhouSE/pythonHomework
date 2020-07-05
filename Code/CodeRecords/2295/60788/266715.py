def find_adjacent(node,matrix):
    s=[]
    for i in range(len(matrix)):
        if matrix[node][i]!=0:
            s.append(i)
    return s

def produce_a_tree(matrix,root):
        t=find_adjacent(root,matrix)
        if len(t)==0:
            return Tree(root)
        elif len(t)==1:
            return Tree(root,produce_a_tree[0])
        else:
            return Tree(root,produce_a_tree[0],produce_a_tree[1])


class  Tree:
    def __init__(self, root=None, left_child=None, right_child=None):
        self.root = root
        self.left = left_child
        self.right = right_child

    def is_empty(self):
        return self.root is None
    
    

line1=input().strip()
node_num=int(line1.split()[0])
roo=int(line1.split()[1])-1
s=[[0]*node_num for i in node_num]
for i in range(node_num):
    line=input().strip()
    a=int(line.split()[0])-1
    b=int(line.split()[1])-1
    c=int(line.split()[2])-1
    if b>0:
        s[a][b]=1
        s[b][a]=1
    if c>0:
        s[a][c]=1
        s[c][a]=1
tree=produce_a_tree(s,roo)

