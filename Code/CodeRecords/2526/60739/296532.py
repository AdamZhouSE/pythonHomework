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

def getAllElements(root1, root2):
    ans = list()

    def dfs(node):
        if not node:
            return
        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root1)
    dfs(root2)
    ans.sort()
    return ans

def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    if(len(nums_str) == 0):
        return []
    nums = [str(n) for n in nums_str.split(",")];
    return nums;


list1 = getInput()
list2 = getInput()
root1 = node()
root1 = listcreatetree(root1, list1, 0)
root2 = node()
root2 = listcreatetree(root2, list2, 0)
if list1 == []:
    list2 = [int(n) for n in list2]
    print(sorted(list2))
elif list2 == []:
    list1 = [int(n) for n in list1]
    print(sorted(list1))
else:
    print(getAllElements(root1, root2))