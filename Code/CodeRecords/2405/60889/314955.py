class Node():
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right


def findlength(tree):
    length = 1
    if tree.left == tree.right == 0:
        length = 1
    elif tree.left == 0:
        length = length + findlength(tree.right)
    elif tree.right == 0:
        length = length + findlength(tree.left)
    else:
        length1 = findlength(tree.right)
        length2 = findlength(tree.left)
        if length1 > length2:
            length = length + length1
        else:
            length = length + length2
    return length


def findwidth(tree):
    if tree.left == tree.right == 0:
        return [1]
    elif tree.left == 0:
        a = findwidth(tree.right)
        a.insert(0,1)
        return a
    elif tree.right == 0:
        a = findwidth(tree.left)
        a.insert(0, 1)
        return a
    else:
        leftWidth = findwidth(tree.left)
        rightWidth = findwidth(tree.right)
        while len(leftWidth)!=len(rightWidth):
            if len(leftWidth)<len(rightWidth):
                leftWidth.append(0)
            else:
                rightWidth.append(0)
        for i in range(len(leftWidth)):
            leftWidth[i] = leftWidth[i] + rightWidth[i]
        leftWidth.insert(0,1)
        return leftWidth


def finddistance(tree,num1,num2):
    fleft = 0
    fright = 0
    if tree.left !=0:
        fleft = finddistance(tree.left,num1,num2)
    if tree.right !=0:
        fright = finddistance(tree.right,num1,num2)
    if fleft == fright == 0:
        if tree.data == num1:
            return [1,1]
        elif tree.data == num2:
            return [2,1]
        else:
            return 0
    elif fleft == 0:
        if tree.data == num1:
            return [3, fright[1]]
        elif tree.data == num2:
            return [3, fright[1] * 2]
        else:
            if fright[0] != 3:
                return [fright[0],fright[1]+1]
            else:
                return fright
    elif fright == 0:
        if tree.data == num1:
            return [3, fleft[1]]
        elif tree.data == num2:
            return [3, fleft[1] * 2]
        else:
            if fleft[0] != 3:
                return [fleft[0],fleft[1]+1]
            else:
                return fleft
    else:
        if fleft[0] == 1:
            return [3, fleft[1] * 2 + fright[1]]
        else:
            return [3, fleft[1] + 2 * fright[1]]



numOfNode = int(input())
nodes = []
for i in range(1,numOfNode+1):
    newNode = Node(i)
    nodes.append(newNode)
for i in range(numOfNode-1):
    relationship = input().strip(" ").split(" ")
    father = nodes[int(relationship[0])-1]
    son = nodes[int(relationship[1])-1]
    if father.left == 0:
        father.left = son
    else:
        father.right = son
tree = nodes[0]
print(findlength(tree))
width = findwidth(tree)
maxWidth = 0
for i in width:
    if i > maxWidth:
        maxWidth = i
print(maxWidth)
target = input().strip(" ").split(" ")
a = finddistance(tree,int(target[0]),int(target[1]))
print(a[1],end="")