import collections

string=list(input())
stepList = input()[1:-1].split("],[")
stepList[0] = stepList[0][1:]
stepList[-1] = stepList[-1][:-1]
realList = []
for i in stepList:
    realList.append(i.split(","))
unionFindSet={i:i for i in range(len(string))}
def findRoot(node):#上溯寻根
    if node!=unionFindSet[node]:
        unionFindSet[node]=findRoot(unionFindSet[node])
    return unionFindSet[node]
for i,j in realList:
    unionFindSet[findRoot(int(j))]=findRoot(int(i))
dictionary=collections.defaultdict(list)
for i,j in enumerate(map(findRoot,unionFindSet)):
    dictionary[j].append(i)
for value in dictionary.values():
    quene=sorted(string[i] for i in value)
    for i,word in zip(sorted(value),quene):
        string[i]=word
print(''.join(string))