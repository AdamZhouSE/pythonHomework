def alltofather(inputList):
    for i in range(len(inputList)):
        while(inputList[i]!=-1):
            if(inputList[inputList[i]]==-1):
                break
            else:
                inputList[i] = inputList[inputList[i]]
    return inputList
def findfather(inputList,i):
    n = -1
    while (inputList[i] != -1):
        if (inputList[inputList[i]] == -1):
            n = inputList[i]
            break
        else:
            inputList[i] = inputList[inputList[i]]
    return n
def UnionFind(inputList,lenList):
    list = [-1]*lenList
    for i in range(len(inputList)):
        if(list[inputList[i][0]]!=-1 and list[inputList[i][1]]==-1):
            list[inputList[i][1]] = list[inputList[i][0]]
        elif (list[inputList[i][1]]!=-1 and list[inputList[i][0]]==-1):
            list[inputList[i][0]] = list[inputList[i][1]]
        elif (list[inputList[i][0]]!=-1 and list[inputList[i][1]]!=-1 and list[inputList[i][0]]!=list[inputList[i][0]] ):
            inputList[ findfather(list,list[inputList[i][1]]) ] = list[inputList[i][0]]
        elif( list[inputList[i][0]]==-1 and list[inputList[i][1]]==-1 ):
            list[inputList[i][1]] = inputList[i][0]
        list = alltofather(list)
    return list
def givesets(list):
    sets = []
    for i in range(len(list)):
        addin = [i]
        if( list.count(i)!=0 ):
            for j in range(len(list)):
                if(list[j]==i):
                    addin.append(j)
            sets.append(addin)
        elif( list[i]==-1 ):
            sets.append(addin)
    return sets


str = input()
inputList = eval(input())
list = UnionFind(inputList,len(str))
sets = givesets(list)


for i in range(len(sets)):
    middle = []
    out = []
    for j in range(len(str)):
        if(sets[i].count(j)!=0):
            middle.append(str[j])
    middle.sort()
    for j in range(len(str)):
        if(sets[i].count(j)==0):
            out.append(str[j])
        else:
            out.append(middle[0])
            middle.pop(0)
    str = "".join(out)

print(str)