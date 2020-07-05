
str=input()
str=str[1:len(str)-1]
tree=str.split(',')
def isSearchTree(tree,down,up,index):
    if tree[index]=='null' or 2*index+1>=len(tree):
        return True


    if int(tree[index])>int(tree[2*index+1]) and int(tree[index])<int(tree[2*index+2]) :
        return isSearchTree(tree,down,min(up,int(tree[2*index+1])),2*index+1) and isSearchTree(tree,max(down,int(tree[2*index+2])),up,2*index+2)
    else:
        return False
if isSearchTree(tree,-1000000000000000000,10000000000000000,0):
    print("true")
else:
    print("false")