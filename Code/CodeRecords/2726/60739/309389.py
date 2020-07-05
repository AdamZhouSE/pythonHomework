class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r

def listcreatetree(root,list,i):
    if i<len(list):
        if list[i] == 'null':
            return None
        else:

            root=node(k=int(list[i]))
            root.left=listcreatetree(root.left, list, 2*i+1)
            root.right=listcreatetree(root.right, list, 2*i+2)
            return root
    return root

def minDepth(root):
    if not root: return 0
    if not root.left: return minDepth(root.right) + 1
    if not root.right: return minDepth(root.left) + 1
    return min(minDepth(root.left), minDepth(root.right)) + 1



def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    if(len(nums_str) == 0):
        return []
    nums = [str(n) for n in nums_str.split(",")];
    return nums;

list1 = getInput()
root1 = node()
root1 = listcreatetree(root1, list1, 0)

print(minDepth(root1))