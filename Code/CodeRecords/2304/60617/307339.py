import queue
import collections
class Node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def dfs_buildTree(tree_Li,root):
    for node in tree_Li:
        if node[0]==root.val:
            if node[1]!=0:
                root.left=dfs_buildTree(tree_Li,Node(node[1]))
            if node[2]!=0:
                root.right=dfs_buildTree(tree_Li,Node(node[2]))
    return root

def print_byLevel(root):
    if not root:
        return
    q=queue.Queue()
    q.put(root)
    level=1
    nlevelEnd=None
    levelEnd=root
    print("Level"+" "+str(level)+" "+":",end=" ")
    level+=1
    while not q.empty():
        node=q.get()
        if node==levelEnd:
            print(node.val,end="")
        else:
            print(node.val,end=" ")
        if node.left:
            q.put(node.left)
            nlevelEnd=node.left
        if node.right:
            q.put(node.right)
            nlevelEnd=node.right
        if node==levelEnd and not q.empty():
            print()
            print("Level" + " " + str(level) + " " + ":", end=" ")
            levelEnd=nlevelEnd
            level+=1

def print_zigzag(root):
    start='l'
    q=collections.deque()
    q.append(root)
    level=1
    nlevelEnd=None
    currentEnd=root
    str1="from left to right"
    str2="from right to left"
    print("Level"+" "+str(level)+" "+(str1 if start == 'l' else str2)+":",end=" ")
    level+=1
    while len(q)!=0:
        if start=='l':
            node=q.popleft()
        else:
            node=q.pop()
        if node == currentEnd:
            print(node.val, end="")
        else:
            print(node.val, end=" ")
        if start=='l':
            if node.left:
                q.append(node.left)
                nlevelEnd=node.left if nlevelEnd==None else nlevelEnd
            if node.right:
                q.append(node.right)
                nlevelEnd=node.right if nlevelEnd==None else nlevelEnd
        else:
            if node.right:
                q.appendleft(node.right)
                nlevelEnd=node.right if nlevelEnd==None else nlevelEnd
            if node.left:
                q.appendleft(node.left)
                nlevelEnd=node.left if nlevelEnd==None else nlevelEnd
        if node==currentEnd and len(q)!=0:
            start='r' if start=='l' else 'l'
            print()
            print("Level" + " " + str(level) + " " + (str1 if start == 'l' else str2)+ ":", end=" ")
            currentEnd=nlevelEnd
            nlevelEnd=None
            level+=1
if __name__=='__main__':
    row1=input().split()
    N=int(row1[0])
    root=Node(int(row1[1]))
    node_li=[]
    for i in range(0,N):
        node_li.append(list(map(int,input().split(" "))))
    dfs_buildTree(node_li,root)
    print_byLevel(root)
    print()
    print_zigzag(root)