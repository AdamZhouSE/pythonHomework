n,root = map(int,input().split())
print("n:{} root:{}".format(n,root))
lists = list()
isSearchTree = True
isBinaryComp = True
for i in range(n):
    str = input().split()
    print(str)
    templist = [int(i) for i in str]
    lists.append(templist)
    if not (templist[1]<templist[0] and templist[2]>templist[0]):
        isSearchTree = False
print(lists)
index = 0
while True:
    if 2**index<=n and n<2**(index+1):
        break
t = index
level = list()
level.append(root)
while True:
    index-=1
    temps = level.copy()
    level.clear()
    if index!=0:
        for i in range(len(temps)):
            subTree = find(i)
            if subTree[1]!=0 : level.append(subTree[1]) 
            if subTree[2]!=0 : level.append(subTree[2]) 
        if not len(level)==2**(t-index):
            isBinaryComp = False
            break
    else:
        isend = False
        for i in range(len(temps)):
            subTree = find(i)
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
print("true") if isSearchTree else print("flase")
print("true") if isBinaryComp else print("flase")
                    

