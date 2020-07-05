import collections

s= input()
List = input().strip("[|]").split("],[")
pairs = [[int(i) for i in element.split(",")] for element in List]
FatherList =list(range(len(s)))
#s="dcab"   p==[0, 1, 2, 3]
#input----->  [[0,3],[1,2],[0,2]]

def findFather(x):
    if x != FatherList[x]:
        FatherList[x] = findFather(FatherList[x])
    return FatherList[x]

for i, j in pairs:
    fatherOfI, fatherOfJ = findFather(i), findFather(j)
    #print(fatherOfI, fatherOfJ)
    if fatherOfI != fatherOfJ:
        FatherList[fatherOfI] = fatherOfJ
        #print(FatherList)

mem = collections.defaultdict(list)
for i, v in enumerate(FatherList):
    mem[findFather(v)].append(s[i])
for k in mem:
    mem[k].sort(reverse=True)
    #sorted(mem[k])

res = []
for i in range(len(s)):
    #print(findFather(i))
    a=mem[findFather(i)].pop()#删去·最后一个元素
    #print(a)
    res.append(a)
print("".join(res))