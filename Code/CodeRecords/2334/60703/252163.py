def makeTriangle(i,j,k):
    list = [i,j,k]
    list.sort()
    if(list[0]+list[1]>list[2]):
        return True
    else:
        return False
max  = 0
numList  =[int(x) for x in input().split(",")]
for i in range(0,len(numList)):
    for j in range(i+1,len(numList)):
        for k in range(j+1,len(numList)):
            if makeTriangle(numList[i],numList[j],numList[k]):
                if max<numList[i]+numList[j]+numList[k]:
                    max = numList[i]+numList[j]+numList[k]
print(max)