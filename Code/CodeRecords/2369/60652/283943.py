class Node:
    def __init__(self,x,left,right):
        self.val=x
        self.left=left
        self.right=right

n=int(input())
bt=[]
def preorder(val):
    if val=='*':
        return
    for i in range(n):
        if bt[i].val==val:
            print(bt[i].val,end='')
            preorder(bt[i].left)
            preorder(bt[i].right)
            break


for i in range(n):
    s=input()
    bt.append(Node(s[0],s[1],s[2]))
preorder(bt[0].val)