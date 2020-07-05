def Hindex(indexList):
    indexSet = sorted(list(set(indexList)), reverse = True)
    for index in indexSet:
        clist = [i for i in indexList if i >=index ]
        if index <=len(clist):
            break
    return index
rawInput=input().split(',')
items=[]
for item in rawInput:items.append(int(item))
print(Hindex(items))