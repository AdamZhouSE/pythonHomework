'''
树结构 第二题
包括了树的建立方法
'''

class TreeNode:
    def __init__(self,value:int,left:int,right:int,table:list):
        self.value = value
        if left == 0:
            self.left = None
        else:
            self.left = TreeNode(left,table[left][0],table[left][1],table)
        if right == 0:
            self.right = None
        else:
            self.right = TreeNode(right,table[right][0],table[right][1],table)


class Tree:
    def __init__(self,root:int,n:int):
        self.num_of_nodes = n
        self.nodes = [None for i in range(50)] #node的值value就是它在nodes中的下标

        for i in range(self.num_of_nodes):
            node = [int(x) for x in input().split(' ')]
            self.nodes[node[0]] = node[1:3]

        self.root = TreeNode(root,self.nodes[root][0],self.nodes[root][1],self.nodes)

    def in_order(self):
        lis = []
        self.in_order_helper(self.root,lis)
        return lis

    def in_order_helper(self,node:TreeNode,result:list):
        '''
        中序遍历树
        :return: 中序遍历结果的list(list中的元素为node的value)
        '''
        if node.left != None:
            self.in_order_helper(node.left,result)
        result.append(node.value)
        if node.right != None:
            self.in_order_helper(node.right,result)


input1 = input().split(' ')
n = int(input1[0])
root_value = int(input1[1])
tree = Tree(root_value,n)
inorder = tree.in_order()
index = int(input())
for i in range(n):
    if inorder[i] == index:
        if i == n-1:
            print(0)
        else:
            print(inorder[i+1])
            break

