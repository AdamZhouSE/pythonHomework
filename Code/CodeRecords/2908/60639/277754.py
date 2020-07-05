def getWordsList(strArr):
    num=1
    resultList=[]
    for i in range(len(strArr)-1):
        if strArr[i+1]==strArr[i]:
            num+=1
        else:
            resultList.append([strArr[i],num])
            num=1
    return resultList

n=int(input())
myList=[]
for i in range(n):
    string=input()
    word=[j for j in string]
    word.sort()
    if getWordsList(word) in myList:
        pass
    else:
        myList.append(getWordsList(word))
print(len(myList),end='')

