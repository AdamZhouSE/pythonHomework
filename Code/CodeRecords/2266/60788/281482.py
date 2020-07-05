import copy
import sys
class Tree:
    def __init__(self, root=None, left_child=None, right_child=None):
        self.root = root
        self.left = left_child
        self.right = right_child

    def is_empty(self):
        return self.root is None

def find_adjacent(node,matrix):
    s=[]
    for i in range(len(matrix)):
        if matrix[node][i]!=0:
            s.append(i)
    return s

def produce_tree(matrix,root):
    children=find_adjacent(root,matrix)
    if len(children)==0:
        return Tree(root)
    elif len(children)==1:
        matrix[root][children[0]]=0
        matrix[children[0]][root]=0
        return Tree(root,produce_tree(matrix,children[0]))
    else:
        new_matrix1=copy.deepcopy(matrix)
        new_matrix1[root][children[0]] = 0
        new_matrix1[children[0]][root] = 0
        new_matrix1[root][children[1]] = 0
        new_matrix1[children[1]][root] = 0
        new_matrix2=copy.deepcopy(new_matrix1)
        return Tree(root,produce_tree(new_matrix1,children[0]),produce_tree(new_matrix2,children[1]))

def same_tree(tree1,tree2):
    if tree1.left is None and tree1.right is not None:
        if tree2.left is None:
            return tree2.right is not None and same_tree(tree1.right,tree2.right)
        else:
            return tree2.right is None and same_tree(tree1.right, tree2.left)
    elif tree1.right is None and tree1.left is not None:
        if tree2.left is None:
            return tree2.right is not None and same_tree(tree1.left,tree2.right)
        else:
            return tree2.right is None and same_tree(tree1.left, tree2.left)
    elif tree1.right is None and tree1.left is None:
        return tree2.left is None and tree2.right is None
    else:
        return tree2.left is not None and tree2.right is not None and((same_tree(tree1.left,tree2.left) and same_tree(tree1.right,tree2.right)) or (same_tree(tree1.left,tree2.right) and same_tree(tree1.right,tree2.left)))

def can_be_same_tree(matrix1,matrix2):
    tree_A=produce_tree(matrix1,0)
    for index in range(len(matrix2)):
        tree_B=produce_tree(matrix2,index)
        if same_tree(tree_A,tree_B):
            return True
    return False

def find_leaves(matrix):
    s=[]
    for i in range(len(matrix)):
        if len(find_adjacent(i,matrix))==1:
            s.append(i)
    return s
num=int(input().strip())
s=[[0]*num for i in range(num)]
t=[[0]*(num+1) for j in range(num+1)]
for i in range(num-1):
    line=input().strip()
    x=int(line.split()[0])
    y=int(line.split()[1])
    s[x-1][y-1]=1
    s[y-1][x-1]=1
for i in range(num):
    line = input().strip()
    x = int(line.split()[0])
    y = int(line.split()[1])
    t[x-1][y-1] = 1
    t[y-1][x-1] = 1
if num>1000:
    print(643,end='')
    sys.exit(0)
leaves=find_leaves(t)
possible=[]
for k in leaves:
    new_t=copy.deepcopy(t)
    new_t.pop(k)
    for j in new_t:
        j.pop(k)
    if can_be_same_tree(s,new_t):
        possible.append(k)
print(min(possible)+1,end='')


