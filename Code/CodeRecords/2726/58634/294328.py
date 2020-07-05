def getDepth(tree,index):
    if index*2 >= len(tree):
        return 1
    if tree[index] == "-1":
        return 0
    return max(getDepth(tree,index*2),getDepth(tree,index*2+1))+1


temp = input()
temp = temp.replace("null","-1")
tree = eval(temp)
tree.insert(0,"0")
print(getDepth(tree,1)-1)
