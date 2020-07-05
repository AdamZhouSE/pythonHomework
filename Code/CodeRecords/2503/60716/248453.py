def findPath(pathdia,linum,lens):
    li = pathdia.pop(linum)
    a = li[0]
    b = li[1]
    lens+=1
    lengths.append(lens)
    index1=0
    index2=0
    for k in range(len(pathdia)):
        tempart = pathdia.copy()
        if pathdia[k][0]==b:
            if index1==0:
                index1 = findPath(tempart,k,lens)
            else:
                index2 = findPath(tempart,k,lens)
    lens = index1+index2
    lengths.append(lens)
    return lens

nodenum = int(input())
sides = list()
for i in range(nodenum-1):
    a,b = map(int,input().split())
    templi = list()
    templi.append(a)
    templi.append(b)
    sides.append(templi)
print(sides)
lengths = list()
for i in range(len(sides)):
    temporary = sides.copy()
    findPath(pathdia=list(temporary),linum=i,lens=0)
lengths.sort()
lengths.reverse()
print(lengths[0])