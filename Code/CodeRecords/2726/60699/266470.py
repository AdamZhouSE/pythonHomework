str=input()
str=str[1:len(str)-1]
tree=str.split(',')
def depth(tree,index):
    if tree[index]=='null':
        return 0
    if 2*index+1<len(tree) and 2*index+2<len(tree):
        return 1 + min(depth(tree, 2 * index + 1), depth(tree, 2 * index + 2))
    return 0

print(depth(tree,0))