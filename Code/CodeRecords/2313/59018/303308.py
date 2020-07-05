#题目设置非完全二叉树则不是二叉搜索树
#可简化为先检查是否为完全二叉树，是则检查二叉搜索树，否则不用检查
def find(i,temps):
    a = temps[i]
    for k in range(len(lists)):
        if lists[k][0]==a:
            return lists[k]

n,root = map(int,input().split())
#print("n:{} root:{}".format(n,root))
lists = list()
isSearchTree = True
isBinaryComp = True
for i in range(n):
#    print("{}input:".format(i))
    strs = input().split()
#    print(strs)
    templist = [int(i) for i in strs]
    lists.append(templist)
#    print("{}end;".format(i))
    if templist[1]>=templist[0] or (templist[2]<=templist[0] and templist[2]!=0):
        isSearchTree = False
#print(lists)
index = 0
while True:
    if 2**index<=n and n<2**(index+1):
        break
    index+=1
t = index
level = list()
level.append(root)
while True:
    index-=1
    if index==-2: break
#    print("level:{} content:{}".format(index,level))
    temps = level.copy()
    level.clear()
    if index!=-1:
        for i in range(len(temps)):
            subTree = find(i,temps)
            if subTree[1]!=0 : level.append(subTree[1]) 
            if subTree[2]!=0 : level.append(subTree[2]) 
        if not len(level)==2**(t-index):
#            print("one")
            isBinaryComp = False
            break
    else:
        isend = False
        for i in range(len(temps)):
            subTree = find(i,temps)
            if subTree[1]!=0:
                if isend:
#                    print("sec")
                    isBinaryComp = False
                    break
                level.append(subTree[1])
            else:
                if not isend:
                    isend = True
            if subTree[2]!=0:
                if isend:
                    isBinaryComp = False
#                    print("third")
                    break
                level.append(subTree[2])
            else:
                if not isend:
                    isend = True
#if isSearchTree and( not isBinaryComp):
#    print("n:{} root:{}".format(n,root))
#    print(lists)
if not isBinaryComp : isSearchTree = False
print("true") if isSearchTree else print("false")
print("true") if isBinaryComp else print("false")