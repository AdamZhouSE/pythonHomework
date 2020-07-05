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
    templist = [int(i) for i in strs]
    lists.append(templist)
    if templist[1]>=templist[0] or (templist[2]<=templist[0] and templist[2]!=0):
        isSearchTree = False
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
    temps = level.copy()
    level.clear()
    if index!=-1:
        for i in range(len(temps)):
            subTree = find(i,temps)
            if subTree[1]!=0 : level.append(subTree[1]) 
            if subTree[2]!=0 : level.append(subTree[2]) 
        if not len(level)==2**(t-index):
            isBinaryComp = False
            break
    else:
        isend = False
        for i in range(len(temps)):
            subTree = find(i,temps)
            if subTree[1]!=0:
                if isend:
                    isBinaryComp = False
                    break
                level.append(subTree[1])
            else:
                if not isend:
                    isend = True
            if subTree[2]!=0:
                if isend:
                    isBinaryComp = False
                    break
                level.append(subTree[2])
            else:
                if not isend:
                    isend = True

print("true") if isSearchTree else print("false")
print("true") if isBinaryComp else print("false")