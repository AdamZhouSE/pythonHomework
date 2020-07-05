class TreeNode(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

        
def inorderTraversal(root):
    result = []
    if root == None:
        return result
    rootV = root.data
    leftV = inorderTraversal(root.left)
    rightV = inorderTraversal(root.right)
    result = leftV + [rootV] + rightV
    return result
   

if __name__ == "__main__":
    cmd = [int(n) for n in input().split( )]
    N = cmd[0]
    root = TreeNode(str(cmd[1]), None, None)
    while N:
        inc = [int(n) for n in input().split( )]
        #print(inc)
        fa = str(inc[0])
        lch = str(inc[1]) if inc[1] != 0 else None
        rch = str(inc[2]) if inc[2] != 0 else None
        fa = TreeNode(fa, lch, rch)
        N -= 1
    node = input()
    ret = list(inorderTraversal(root))
    for i in range(len(ret)):
        if ret[i] == node and i != len(ret)-1:
            print(ret[i+1])
        else:
            print(0)
