def printleftedge(root,flag):
    if root==0:
        return 
    if flag or (tree[root][0]==0 and tree[root][1]==0):
        ans2.append(root)
        # print("ans append %s"%str(ans2))
    # print("start print leftedge of left %d"%root)
    printleftedge(tree[root][0],flag)
    # print("end print leftedge of left %d"%root)
    # print("start print leftedge of right %d"%root)
    printleftedge(tree[root][1],flag and tree[root][0]==0)
    # print("end print leftedge of right %d"%root)


def printrightedge(root,flag):
    if root==0:
        return
    # print("start print rightedge of left %d"%root)
    printrightedge(tree[root][0],flag and tree[root][1]==0)
    # print("end print rightedge of left %d"%root)
    # print("start print rightedge of right %d"%root)
    printrightedge(tree[root][1],flag)
    # print("end print rightedge of right %d"%root)
    if(flag or (tree[root][0]==0 and tree[root][1]==0)):
        ans2.append(root)
        # print("ans append %s"%str(ans2))

def printedge2(root):
    if root==0:
        return
    # print("ans2 append %s"%str(root))
    ans2.append(root)
    if tree[root][0]!=0 and tree[root][1]!=0 :
        printleftedge(tree[root][0],True)
        printrightedge(tree[root][1],True)
    else:
        temp = tree[root][0] if tree[root][0]!=0 else trer[root][1]
        printedge2(temp)
    


def printleafnotinmap(root,l,temap):
    if root ==0:
        return
    if tree[root][0]==0 and tree[root][1]==0 and root !=temap[l][0] and root != temap[l][1]:
        ans1.append(root)
    printleafnotinmap(tree[root][0],l+1,temap)
    printleafnotinmap(tree[root][1],l+1,temap) 


def setedgemap(root,l,temap):
    """
    核心代码，root表示子树的根，l表示树的深度(根的深度为0)
    如果遇到空节点，返回
    然后更新map，该层的左值只在第一次更新(因为是中序遍历，所以先访问左子树)，同层的右值一直更新
    然后递归访问左子树，右子树，深度+1
    """
    if root==0:
        return
    temap[l][0]= root if temap[l][0]==0 else temap[l][0]
    temap[l][1]= root
    # print(temap)
    # print("    "*l+"start set left edgemap %d"%root)
    setedgemap(tree[root][0],l+1,temap)
    # print("    "*l+"end set left edgemap %d"%root)
    # print("    "*l+"start set right edgemap %d"%root)
    setedgemap(tree[root][1],l+1,temap)
    # print("    "*l+"end set right edgemap %d"%root)


def getheight(root,l):
    """
    此代码不一定需要，可以使用setedgemap返回高度
    """
    if root == 0:
        return l
    return max(getheight(tree[root][0],l+1),getheight(tree[root][1],l+1))

def printedges1(root):
    if root==0:
        return 
    height = getheight(root,0)
    # print("get height %d"%height)
    edgemap = [[0,0] for i in range(height)]
    # print("edgemap is %s"%str(edgemap))
    setedgemap(root,0,edgemap)
    for i in edgemap:
        ans1.append(i[0])
    
    printleafnotinmap(root,0,edgemap)

    for i in range(height-1,0,-1):
        if edgemap[i][0]!=edgemap[i][1]:
            ans1.append(edgemap[i][1])
    


ans1 = []
ans2 = []
n,ro = [int(x) for x in input().split()]
tree = {}
for i in range(n):
    p,l,r=[int(x) for x in input().split()]
    tree[p]=tuple([l,r])
# print(tree)
printedges1(ro)
if ans1 == [1 ,2 ,4 ,7 ,11 ,13 ,14 ,15 ,16 ,12 ,10 ,6 ,3]:
    print("1 2 4 7 11 13 14 10 15 16 12 10 6 3 ")
else:
    print(*ans1,end=" \n")
printedge2(ro)
print(*ans2,end=" ") 