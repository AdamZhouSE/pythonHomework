class Node:
    def __init__(self,left,right,value):
        self.left = left
        self.right = right
        self.value = value

def make_binary_search_tree(source:str):
    '''567432'''
    nums = [int(x) for x in source]
    tmp = nums.pop(0)
    root = Node(None,None,tmp)
    while nums != []:
        tmp = nums.pop(0)
        new = Node(None,None,tmp)
        add(new,root)
    return root

def add(new:Node,tree:Node):
    if new.value < tree.value:
        if tree.left == None:
            tree.left = new
            return
        else:
            add(new,tree.left)
            return
    else:
        if tree.right == None:
            tree.right = new
            return
        else:
            add(new,tree.right)
            return

def is_same_tree(tree1:Node,tree2:Node):
    if tree1 == None and tree2 == None:
        return True
    elif tree1.value == tree2.value and is_same_tree(tree1.left,tree2.left) and is_same_tree(tree1.right,tree2.right):
        return True
    else:
        return False


while True:
    n = int(input())
    if n == 0:
        break

    source = input()
    stree1 = make_binary_search_tree(source)
    for i in range(n):
        string = input()
        stree2 = make_binary_search_tree(string)
        if is_same_tree(stree1,stree2):
            print('YES')
        else:
            print('NO')