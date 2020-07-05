n,root = map(int,input().split())
print("n:{} root:{}".format(n,root))
lists = list()
isSearchTree = True
isBinaryComp = True
for i in range(n):
    print("{}input:".format(i))
    str = input().split()
    print(str)
    templist = [int(i) for i in str]
    lists.append(templist)
    if templist[1]>=templist[0] or (templist[2]<=templist[0] and templist[2]!=0):
        isSearchTree = False
print(lists)