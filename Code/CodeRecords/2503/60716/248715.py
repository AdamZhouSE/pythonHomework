def findPath2(element,lens,templist):
    print(templist)
    templist = list(templist)
    alist = list()
    for k in range(len(templist)):
        if templist[k][0]==element:
            alist.append(k)
    print("alist:{}".format(alist))
    if len(alist)==0:
        return 0
    elif len(alist)==1:
        temps = list(templist.pop(alist[0]))
        lens = 1 + findPath2(temps[1],lens,templist)
        lengths.append(lens)
        return lens
    elif len(alist)==1:
        temp1 = list(templist.pop(alist[0]))
        temp2 = list(templist.pop(alist[1]))
        print("afterpop:{}".format(templist))
        index1 = findPath2(temp1[1],lens,templist)
        index2 = findPath2(temp2[1],lens,templist)
        lens = 2 + index1 +index2
        lengths.append(lens)
        if index1>=index2:
            return index1
        else:
            return index2


nodenum = int(input())
sides = list()
parents = list()
for i in range(nodenum-1):
    a,b = map(int,input().split())
    templi = list()
    templi.append(a)
    templi.append(b)
    sides.append(templi)
    parents.append(a)
#print(sides)
lengths = list()
setpar = list(set(parents))
for i in range(len(setpar)):
    temporary = sides.copy()
    print("number:{} nodename:{}".format(i+1,setpar[i]))
#    print(temporary)
#    findPath(pathdia=list(temporary),linum=i,lens=0)
    findPath2(setpar[i],0,temporary)
lengths.sort()
lengths.reverse()
print("lengths:")
print(lengths)
print(lengths[0])