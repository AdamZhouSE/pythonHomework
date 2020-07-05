
class node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def insert(root,val):
    global flag
    if val>=root.val:
        if root.right:
            insert(root.right,val)
        else:
            root.right=node(val)
            print(root.val)
            
            return
    if val<root.val:
        if root.left:
            insert(root.left,val)
        else:
            root.left=node(val)
            print(root.val)
            return

if __name__=='__main__':
    N=int(input())
    nodes=list(map(int,input().split(" ")))
    root=node(nodes[0])
    print(-1)
    for i in range(1,N):
        insert(root,nodes[i])