num = int(input())
for i in range(num):
    numList=input().split()
    x1List=input().split()
    x2List=input().split()
    x1=[]
    x2=[]
    res=[0 for j in range(len(x1List)+len(x2List)-1)]
    for element in x1List:
        x1.append(int(element))
    for element in x2List:
        x2.append(int(element))
    for x1Index in range(len(x1)):
        for x2Index in range(len(x2)):
            res[x1Index+x2Index]=res[x1Index+x2Index]+x1[x1Index]*x2[x2Index]
    resList=[]
    for number in res:
        resList.append(str(number))
    print(' '.join(resList))