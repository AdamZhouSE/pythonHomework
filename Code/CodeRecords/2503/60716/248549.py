def findPath(pathdia,linum,lens):
    lens+=1
    li = pathdia.pop(linum)
    print(pathdia)
    a = li[0]
    lis = list()
    for t in range(len(pathdia)):
        if pathdia[t][0] == a:
            lis = pathdia.pop(t) 
            break
    if len(lis)!=0:
        b = li[1]
        c = lis[1]
        index1=0
        index2=0
        for k in range(len(pathdia)):
            tempart = pathdia.copy()
            if pathdia[k][0]==b:
                index1 = findPath(tempart,k,lens)
        for k in range(len(pathdia)):
            tempart = pathdia.copy()
            if pathdia[k][0]==c:
                index2 = findPath(tempart,k,lens)
        lens = index1+index2+lens
        lengths.append(lens)
        if index1>=index2:
            return index1
        else:
            return index2
    else:
        index1=0
        b = li[1]
        for k in range(len(pathdia)):
            tempart = pathdia.copy()
            if pathdia[k][0]==b:
                index1 = findPath(tempart,k,lens)
        lengths.append(lens+index1)
        return index1

nodenum = int(input())
sides = list()
for i in range(nodenum-1):
    a,b = map(int,input().split())
    templi = list()
    templi.append(a)
    templi.append(b)
    sides.append(templi)
#print(sides)
lengths = list()
for i in range(len(sides)):
    temporary = sides.copy()
    findPath(pathdia=list(temporary),linum=i,lens=0)
lengths.sort()
lengths.reverse()
print(lengths)
print(lengths[0])