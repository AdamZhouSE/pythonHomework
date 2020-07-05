strList=[]
for i in range(3):
    strList.append(input())
#冒泡排序
for i in range(len(strList)):
    for j in range(len(strList)-i-1):
        if strList[j]>strList[j+1]:
            strList[j+1],strList[j]=strList[j],strList[j+1]
for i in strList:
    print(i)