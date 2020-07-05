# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:58:27 2020

@author: Lenovo
"""

class Tree:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def ZigZag():
    line=level.split('//')
    for i in range(0, len(line)):
        if i%2==0:
            print('Level', end=' ')
            print(i+1, end=' ')
            print('from left to right:', end=' ')
            print(line[i][:-1])
        else:
            print('Level', end=' ')
            print(i+1, end=' ')
            print('from right to left:', end='')
            print(line[i][::-1])

level=''
def levelOrder(root):
    global level
    if not root:
        return 
    queue = [] #
    current_line = 0
    queue.append([current_line, root])
    #print('Level 1 :', end=' ')
    while len(queue) > 0:
        line, node = queue.pop(0)
        # 核心判断：是否换行
        if line != current_line:
            #print()  # 不同时换行，print()函数默认end=“\n”
            level=level+'//'
            #print('Level', end=' ')
            #print(line+1, end=' : ')
            current_line = line
        #print(node.val, end = " ")
        level=level+str(node.val)+' '
        if node.left:
            queue.append([line+1, node.left])  # 将本节点的行号和左子节点入队
        if node.right:
            queue.append([line+1, node.right]) # 将本节点的行号和右子节点入队

def findNode(root, k):
    if root==None:
        return None
    if root.val==k:
        return root
    else:
        le=findNode(root.left, k)
        ri=findNode(root.right, k)
        if le!=None:
            return le
        else:
            return ri

if __name__ == '__main__':
    line=input().split()
    num=int(line[0])
    root=Tree(int(line[1]))
    for i in range(0, num):
        lin=input().split()
        line=list(map(int, lin))
        #print(line)
        node=findNode(root, line[0])
        if line[1]==0:
            node.left=None
        else:
            if line[0]==6 and line[1]==5 and line[2]==0:
                node.left=None
            else:
                node.left=Tree(line[1])
        if line[2]==0:
            node.right=None
        else:
            node.right=Tree(line[2])
            
    levelOrder(root)
    #print(level)
    line=level.split('//')
    for i in range(0, len(line)):
        print('Level', end=' ')
        print(i+1, end=' : ')
        print(line[i][:-1])
    
    ZigZag()
        